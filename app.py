from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from routes import users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.include_router(users.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="TEC4-BACKEND",
        version="1.0.0",
        description="This is a fantastic API 0_0",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://example.com/logo.png",
        "backgroundColor": "#FFFFFF",
        "altText": "Your Logo",
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/docs", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API documentation")


@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi_schema


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
