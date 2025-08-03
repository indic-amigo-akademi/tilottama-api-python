import joblib
import re
import spacy
from ml_models.utils import words_to_number

intent_model = spacy.load("./ml_models/intent_model")
params_model = spacy.load("./ml_models/params_model")


def extract_number(text):
    try:
        return int(text)
    except ValueError:
        return words_to_number(text)


def extract_add_params(param_doc):
    extracted_params = []
    for ent in param_doc.ents:
        if ent.label_ == "NUMBER":
            try:
                extracted_params.append(extract_number(ent.text))
                print(ent.text)
            except ValueError:
                pass  # Handle cases where entity recognized as number isn't an int
    return extracted_params


def extract_weather_params(param_doc):
    extracted_params = []
    for ent in param_doc.ents:
        if ent.label_ == "CITY":
            extracted_params.append(ent.text)
    return extracted_params


def predict_intent_and_params(text: str):
    """
    Predicts the intent and parameters of a given text.

    Args:
        text (str): The text to predict the intent and parameters for.

    Returns:
        tuple: A tuple containing the predicted intent and parameters.
    """
    intent_doc = intent_model(text)
    predicted_intent = max(intent_doc.cats, key=lambda k: intent_doc.cats[k])

    # Extract parameters using NER
    param_doc = params_model(text)

    if predicted_intent == "calc:add":
        extracted_params = extract_add_params(param_doc)
    elif predicted_intent == "weather:city":
        extracted_params = extract_weather_params(param_doc)
    else:
        extracted_params = []

    return predicted_intent, extracted_params


# if __name__ == "__main__":
#     while True:
#         try:
#             user_text = input("User: ")
#             intent, params = predict_intent_and_params(user_text)
#             print(f"Intent: {intent}")
#             print(f"Params: {params}")
#         except KeyboardInterrupt:
#             print("Exiting...")
#             break
