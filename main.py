import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings.config import get_config
from settings.connector import create_model_table
from settings.routers import api


app = FastAPI()
settings = get_config()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.on_event('startup')(create_model_table)
app.include_router(api)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=1, reload=True)

