import sqlite3
from pathlib import Path
from typing import Dict, List, Optional

DB_PATH = Path("app.db")

def init_db():

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                descripcion TEXT NOT NULL,
                cantidad INTEGER NOT NULL
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

def add_producto(nombre: str, descripcion: str, cantidad: int) -> int:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, cantidad) VALUES (?,?,?)",
            (nombre, descripcion, cantidad)
        )
        conn.commit()
        producto_id = cursor.lastrowid
        print(f"Se agrego el producto {nombre}, con la cantidad {cantidad}")
        return producto_id
    
def search_producto(nombre: str) -> List[Dict[str, Optional[str]]]:
    with get_conn() as conn:
        cursor = conn.execute(
            "SELECT id, nombre, descripcion, cantidad FROM productos WHERE productos.nombre = ? ", (nombre)
        )
        rows = cursor.fetchall()

    result = [
        {
            "id": row[0],
            "nombre": row[1],
            "descripcion": row[2],
            "cantidad": row[3],
        }
        for row in rows
    ]
    print("El producto es: %s", result)
    return result

def delete_producto(id: int):
    with get_conn() as conn:
        cursor = conn.execute(
            "DELETE * FROM producto WHERE producto.id = ?", (id)
        )
        cursor.commit()
        print(f"El producto con id {id} fue eliminado")