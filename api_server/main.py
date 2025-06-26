from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from api_server.routers import weather, currency, forecast
from dotenv import load_dotenv
import os

load_dotenv()

version = os.getenv("VERSION", "1.0.0")
app = FastAPI(
    title="Tilottama API",
    version=version,
    swagger_ui_parameters={"syntaxHighlight": {"theme": "dracula"}},
    root_path="/api/v1",
)

app.include_router(weather.router)
app.include_router(currency.router)
app.include_router(forecast.router)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url or "",
        title=f"{app.title} - Swagger UI",
        swagger_favicon_url="/static/favicon.ico",  # Change this URL to your custom icon URL
    )


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")


@app.get("/")
async def index():
    """
    Get the index page of the API
    """
    return {
        "success": True,
        "message": "Welcome to the {title} v{version}!".format(
            title=app.title, version=app.version
        ),
    }
