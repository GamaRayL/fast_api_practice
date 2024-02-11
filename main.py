from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()

SQLALCHEMY_DATABASE_URL = 'postgresql://user=postgres:password=1612@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
