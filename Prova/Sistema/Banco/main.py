from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
import database

app = FastAPI()

# Inicializa o banco de dados
database.Base.metadata.create_all(bind=database.engine)

# Função para obter uma sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()