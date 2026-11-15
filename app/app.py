import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

VERSION = "1.0.0"

store = {}


class Config(BaseModel):
    name: str
    value: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": VERSION}


@app.get("/env")
def env():
    return {"environment": os.getenv("ENVIRONMENT", "")}


@app.post("/config")
def create_config(config: Config):
    store[config.name] = config.value
    return config


@app.get("/config/{name}")
def get_config(name: str):
    if name not in store:
        raise HTTPException(404)

    return {
        "name": name,
        "value": store[name]
    }


@app.delete("/config/{name}")
def delete_config(name: str):
    if name not in store:
        raise HTTPException(404)

    del store[name]

    return {"deleted": True}

    
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8080"))
    )
