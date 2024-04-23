from sqlalchemy import Column, Integer, String
from fastapi import FastAPI, HTTPException, status
from database import Base

class Professor(Base):
    id_professor: int
    nome: str
    email: str
    cpf: str
    senha: str

class atividades(Base):
    id_atividade: int
    atividade: str

class turmas(Base):
    id_turma: int
    nome_turma: str
    id_professor: int

class adicionar_atividade(Base):
    id_add: int
    id_turma: int
    id_atividade: int