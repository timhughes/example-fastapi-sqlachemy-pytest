from fastapi import FastAPI
from starlette.requests import Request

from . import settings
from .db import base  # noqa:
from .db.session import Session
from .routes import router as api_router


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, debug=settings.DEBUG,
        version=settings.VERSION
    )
    application.include_router(
        api_router, prefix=settings.API_PREFIX,
    )
    return application


app = get_application()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response
