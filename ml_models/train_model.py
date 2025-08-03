import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import json
import spacy
from spacy.training import Example
from spacy.util import minibatch
import random
from utils import words_to_number
import logging

logging.basicConfig(level=logging.INFO)


training_data = json.load(open("data/intent.json"))

# --- Prepare data for Intent Classification ---
intent_training_data = []
for entry in training_data:
    intent_training_data.append((entry["text"], entry["intent"]))

# --- Prepare data for Named Entity Recognition (NER) ---
ner_training_data = []
for entry in training_data:
    entities = []
    if entry["intent"] == "calc:add" and entry["params"]:
        # Simple extraction for numbers (assuming they are digits in the text)
        for param in entry["params"]:
            param_str = str(param)

            start_idx = entry["text"].find(param_str)
            if start_idx != -1:
                end_idx = start_idx + len(param_str)
                entities.append((start_idx, end_idx, "NUMBER"))
    elif entry["intent"] == "weather:city" and entry["params"]:
            city_name = entry["params"][0]
            start_idx = entry["text"].find(city_name)
            if start_idx != -1:
                end_idx = start_idx + len(city_name)
                entities.append((start_idx, end_idx, "CITY"))

    if entities:  # Only add if there are entities to train on
        ner_training_data.append((entry["text"], {"entities": entities}))
logging.info(ner_training_data)

# --- Training Intent Classification ---
nlp_intent = spacy.blank("en")

# Add the TextCategorizer component
textcat = nlp_intent.add_pipe("textcat", last=True)

# Add labels
for _, intent in intent_training_data:
    textcat.add_label(intent)

# Prepare examples for spaCy training
intent_examples = []
for text, intent in intent_training_data:
    intent_examples.append(
        Example.from_dict(nlp_intent.make_doc(text), {"cats": {intent: True}})
    )

# Train the TextCategorizer (simplified training loop for small data)
optimizer = nlp_intent.begin_training()
for i in range(20):  # Number of training iterations
    random.shuffle(intent_examples)
    losses = {}
    nlp_intent.update(intent_examples, drop=0.5, sgd=optimizer, losses=losses)
    # print(f"Iteration {i+1} Losses: {losses}")

logging.info("SpaCy TextCategorizer trained.")
nlp_intent.to_disk("ml_models/intent_model")
logging.info("Intent classifier saved.")


# --- Training Named Entity Recognition (NER) ---.
nlp_params = spacy.load("en_core_web_md")
# Get the NER component
if "ner" not in nlp_params.pipe_names:
    ner = nlp_params.add_pipe("ner", last=True)
else:
    ner = nlp_params.get_pipe("ner")

# Add new labels
labels = [x[2] for x in ner_training_data[0][1]["entities"]]
for label in labels:
    ner.add_label(label)

# Disable other pipes during NER training to focus on NER
other_pipes = [pipe for pipe in nlp_params.pipe_names if pipe != "ner"]
with nlp_params.disable_pipes(*other_pipes):
    optimizer = nlp_params.begin_training()
    for epoch in range(30):  # More iterations might be needed for NER
        random.shuffle(ner_training_data)
        losses = {}
        for batch in minibatch(ner_training_data, size=2):
            for text, annotations in batch:
                example = Example.from_dict(nlp_params.make_doc(text), annotations)
                nlp_params.update([example], drop=0.5, losses=losses)
        logging.debug(f"Losses at epoch {epoch}: {losses}")

logging.info("SpaCy NER trained.")
nlp_params.to_disk("ml_models/params_model")
logging.info("NER model saved.")

# Example prediction
doc = nlp_params("add ten and eleven")
for ent in doc.ents:
    logging.debug(f"Entity: {ent.text}, Label: {ent.label_}")
