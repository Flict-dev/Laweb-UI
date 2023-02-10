import aioredis
from decouple import config
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup():
    db_url = config("DB_URL")
    password = config("DB_PASSWORD")
    redis = await aioredis.from_url(url=db_url, password=password)
