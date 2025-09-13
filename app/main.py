from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_redoc_html
)
from pathlib import Path
import uvicorn

from app.settings import settings
from app.api.api_v1.api import api_router

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    docs_url=None,
    redoc_url=None
)

# Include API routes
app.include_router(api_router, prefix=settings.API_V1_STR)

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
    return {"Hello": "Fast API!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
