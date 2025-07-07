from typing import Dict, List, Optional
from services.service_b import database_producto


def create_producto(nombre: str, descripcion: str, cantidad: int) -> Dict[str, Optional[str]]:

    producto_id = database_producto.add_producto(nombre, descripcion, cantidad)
    user = {
        "id": producto_id,
        "nombre": nombre,
        "descripcion": descripcion,
        "cantidad": cantidad
    }
    return cantidad


def get_all_user(nombre: str) -> List[Dict[str, Optional[str]]]:
    try:
        nombre = database_producto.search_producto(nombre)
        return nombre
    except Exception as exc:
        print("Error al recuperar el producto")
        return []
    
def delete_producto(id: int):
    try:
        database_producto.delete_producto()
    except Exception as exc:
        print(f"Error al eliminar al producto con id: {id}")