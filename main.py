from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.database import create_tables
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "AI-powered personalized fitness plan generator "
        "using Google Gemini."
    ),
    version="1.0.0",
    debug=settings.DEBUG,
    lifespan=lifespan,
)


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)


app.include_router(router)


@app.get("/api")
def api_root():
    return {
        "application": settings.APP_NAME,
        "version": "1.0.0",
        "message": "FitBuddy API is running.",
    }