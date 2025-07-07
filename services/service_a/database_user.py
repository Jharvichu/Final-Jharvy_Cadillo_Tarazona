import sqlite3
from pathlib import Path
from typing import Dict, List, Optional

DB_PATH = Path("app.db")

def init_db():

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombres TEXT NOT NULL UNIQUE,
                apellidos TEXT NOT NULL,
                edad INTEGER
            )
            """
        )
        conn.commit()

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

def add_user(nombres: str, apellidos: str, edad: int) -> int:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (nombres, apellidos, edad) VALUES (?,?,?)",
            (nombres, apellidos, edad)
        )
        conn.commit()
        user_id = cursor.lastrowid
        print(f"Persona {apellidos},{nombres} con edad {edad} : {user_id}")
        return user_id
    
def list_users() -> List[Dict[str, Optional[str]]]:
    with get_conn() as conn:
        cursor = conn.execute(
            "SELECT id, nombres, apellidos, edad FROM users"
        )
        rows = cursor.fetchall()

    result = [
        {
            "id": row[0],
            "nombres": row[1],
            "apellidos": row[2],
            "edad": row[3],
        }
        for row in rows
    ]
    print("Listado de ítems: %s", result)
    return result

def delete_user(id: int):
    with get_conn() as conn:
        cursor = conn.execute(
            "DELETE * FROM users WHERE (? = users.id)", (id)
        )
        cursor.commit()
        print(f"La persona con id {id} fue eliminada")