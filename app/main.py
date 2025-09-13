from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_redoc_html
)

import uvicorn
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(docs_url=None, redoc_url=None)

# 挂载静态文件目录（相对于项目根目录）
app.mount("/static", StaticFiles(directory=BASE_DIR/'static'), name="static")

@app.get("/docs",include_in_schema=False)
def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css"
    )

@app.get("/redoc",include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js"
    )

@app.get("/")
def greet():
    return {"Hello":"Fast API!"}


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
