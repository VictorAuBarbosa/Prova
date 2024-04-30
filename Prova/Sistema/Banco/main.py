from fastapi import FastAPI, HTTPException
import aiomysql
import models
import database

# Configurações do banco de dados MySQL
MYSQL_HOST = "Conforto na Alma"
MYSQL_USER = "root"
MYSQL_PASSWORD = "admin"
MYSQL_DB = "prova"

# Inicializa o aplicativo FastAPI
app = FastAPI()

# Função para criar uma conexão com o banco de dados
async def get_mysql_connection():
    return await aiomysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB
    )

# Rota para criar um novo item no banco de dados
@app.post("/items/")
async def create_item(name: str, description: str):
    async with get_mysql_connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
            item_id = cur.lastrowid
            await conn.commit()
    return {"id": item_id, "name": name, "description": description}

# Rota para obter um item por ID do banco de dados
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    async with get_mysql_connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT id, name, description FROM items WHERE id = %s", (item_id,))
            row = await cur.fetchone()
            if not row:
                raise HTTPException(status_code=404, detail="Item not found")
            item_id, name, description = row
    return {"id": item_id, "name": name, "description": description}