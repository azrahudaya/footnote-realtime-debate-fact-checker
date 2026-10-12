import time

from fastapi import FastAPI
from pydantic import BaseModel

from footnote import __version__


class HealthResponse(BaseModel):
    status: str
    version: str
    uptime_s: int


def create_app() -> FastAPI:
    app = FastAPI(title="Footnote", version=__version__)
    created_at = time.monotonic()

    @app.get("/api/v1/health", response_model=HealthResponse)
    async def health() -> HealthResponse:
        return HealthResponse(
            status="ok",
            version=__version__,
            uptime_s=int(time.monotonic() - created_at),
        )

    return app
