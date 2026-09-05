# ${{ values.name }} — FastAPI service (Gurujix golden path)
from fastapi import FastAPI

app = FastAPI(
    title="${{ values.name }}",
    description="${{ values.description }}",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness: process is up."""
    return {"status": "ok"}


@app.get("/ready")
def ready() -> dict[str, str]:
    """Readiness: safe to receive traffic."""
    return {"status": "ready"}
