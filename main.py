from contextlib import asynccontextmanager

from fastapi import FastAPI

from db import create_tables, delete_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("database is ready")

    yield

    print("database cleared")
    await delete_tables()


app = FastAPI(lifespan=lifespan)
app.include_router(router)
