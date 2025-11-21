from fastapi import FastAPI

from .api.router import api_router


app = FastAPI(
    title="Family Law Case Analysis API",
    description="Backend service skeleton for the Family Law Case Analysis Tool",
    version="0.1.0",
)

app.include_router(api_router)


@app.get("/health", tags=["system"])
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
