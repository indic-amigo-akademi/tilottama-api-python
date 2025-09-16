from fastapi import APIRouter
from ml_models.nlp_intent import predict_intent_and_params
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/core",
    tags=["Core"],
    responses={404: {"description": "Not found"}, 200: {"success": True}},
)


class AppIntent(BaseModel):
    message: str = Field("Hello World", min_length=1)


@router.post("/intent")
async def app_intent(request: AppIntent):
    intent, params = predict_intent_and_params(request.message)
    return {
        "success": True,
        "message": "Intent predicted successfully!",
        "data": {
            "intent": intent,
            "params": params,
        },
    }


@router.post("/reply")
async def app_reply(request: AppIntent):
    intent, params = predict_intent_and_params(request.message)
    if intent == "calc:add":
        reply = f"The sum of {params[0]} and {params[1]} is {params[0] + params[1]}"
    elif intent == "weather:city":
        reply = f"The weather in {params[0]} is cloudy."
    elif intent == "greet:hello":
        reply = "Hello!"
    elif intent == "greet:bye":
        reply = "Goodbye!"
    else:
        reply = "I'm sorry, I don't understand your request."
    return {
        "success": True,
        "message": "Bot reply generated successfully!",
        "data": {
            "reply": reply,
            "intent": intent,
            "params": params,
        },
    }
