from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_redoc_html
)
from pathlib import Path
import uvicorn

from app.core.config import settings
from app.core.logger import setup_logging   

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title=settings.APP_NAME,
    docs_url=None,
    redoc_url=None,
    on_startup=[setup_logging],
)


# Mount static files directory
app.mount("/static", StaticFiles(directory=BASE_DIR/'static'), name="static")


@app.get("/docs", include_in_schema=False)
def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css"
    )


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js"
    )


@app.get("/")
def greet():
    return {"message": f"Hello from Fast API({settings.APP_ENV})!"}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)
