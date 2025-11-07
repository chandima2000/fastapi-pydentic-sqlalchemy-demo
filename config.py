from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()


# CONNECTION_STRING = postgresql://postgres:123456@localhost:5432/fastapi-demo


# Load Database Connection String
connection_string = os.environ["CONNECTION_STRING"]

engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)