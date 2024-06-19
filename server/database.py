import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DB_USER = os.environ.get("DB_USER")
# DB_PASSWORD = os.environ.get("DB_PASSWORD")
# DB_NAME = os.environ.get("DB_NAME")
# DB_URL = os.environ.get("DB_URL")
# DB_PORT = os.environ.get("DB_PORT")
DB_USER = "root"
DB_PASSWORD = "test1234"
DB_NAME = "memento_ai"
DB_URL = "localhost"
DB_PORT = "5555"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_URL}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
