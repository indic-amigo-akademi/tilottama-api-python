from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

load_dotenv()

from api_server.routers import weather, currency, forecast, core

templates = Jinja2Templates(directory="templates")
version = os.getenv("VERSION", "1.0.0")
prefix = os.getenv("PREFIX", "/api/v{version}".format(version=version.split(".")[0]))
app = FastAPI(
    title="Tilottama API",
    version=version,
    swagger_ui_parameters={"syntaxHighlight": {"theme": "dracula"}},
)

app.include_router(weather.router, prefix=prefix)
app.include_router(forecast.router, prefix=prefix)
app.include_router(currency.router, prefix=prefix)
app.include_router(core.router, prefix=prefix)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url or "",
        title=f"{app.title} - Swagger UI",
        swagger_favicon_url="/favicon.ico",  # Change this URL to your custom icon URL
    )


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")


@app.get(prefix, include_in_schema=False)
async def api_index():
    """
    Get the index page of the API
    """
    return {
        "success": True,
        "message": "Welcome to the {title} v{version}!".format(
            title=app.title, version=app.version
        ),
        "data": {
            "routes": [
                {
                    "name": route.name,
                    "path": route.path,
                    "methods": route.methods,
                    "summary": route.endpoint.__doc__.strip().split("\n")[0],
                }
                for route in app.routes
                if route and route.path.startswith(prefix)
            ]
        },
    }


@app.get("/", include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse("index.j2", {"request": request})


@app.get("/app", include_in_schema=False)
async def web_app(request: Request):
    return templates.TemplateResponse("app.j2", {"request": request})
