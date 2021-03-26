from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

DATABASE_URL = "postgresql://docker:password@db:5432/apartments_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

books = Table(
    "book",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("primary_author", String),
)


def init_db():
    with engine.connect() as con:
        data = (
            {"id": 1, "title": "The Hobbit", "primary_author": "Tolkien"},
            {"id": 2, "title": "The Silmarillion", "primary_author": "Tolkien"},
            {"id": 3, "title": "Yet Another Title", "primary_author": "John Doe"},
        )
        statement = text(
            """INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)"""
        )
        for line in data:
            con.execute(statement, **line)


def get_data_db():
    with engine.connect() as con:
        rs = con.execute("SELECT * FROM book")
        for row in rs:
            yield row


app = FastAPI()


@app.get("/")
def home():
    Base.metadata.create_all(bind=engine)

    if len(list(get_data_db())) < 1:
        init_db()

    return {"books": list(get_data_db())}
