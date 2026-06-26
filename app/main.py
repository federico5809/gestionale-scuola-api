from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core import db
from app.api.graphql.router import graphql_router, GraphQLRouter


@asynccontextmanager
async def lifespan(_app: FastAPI): # il "_" mi è stato consigliato da chat col fatto che "app" non mi serve
    await db.start()
    yield
    await db.stop()


app = FastAPI(lifespan=lifespan)

app.include_router(graphql_router, prefix="/graphql")