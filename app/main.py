from fastapi import FastAPI
from app.routers import currency
from dotenv import load_dotenv
import os

load_dotenv()

version = os.getenv("VERSION", "1.0.0")
app = FastAPI(title="Tilottama API", version=version)

app.include_router(currency.router, prefix="/api/v1/currency")


@app.get("/")
async def root():
    return {
        "success": True,
        "message": "Welcome to the {title} v{version}!".format(
            title=app.title, version=app.version
        ),
    }
