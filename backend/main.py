from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import os

app = FastAPI()

# Modelo de dados para o cadastro
class Usuario(BaseModel):
    nome: str
    email: str

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user="root",
        password="rootpassword",
        database="app_db"
    )

@app.get("/usuarios")
def listar_usuarios():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    resultado = cursor.fetchall()
    db.close()
    return resultado

@app.post("/usuarios")
def cadastrar_usuario(usuario: Usuario):
    db = get_db()
    cursor = db.cursor()
    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    cursor.execute(sql, (usuario.nome, usuario.email))
    db.commit()
    db.close()
    return {"mensagem": "Usuário cadastrado com sucesso!"}