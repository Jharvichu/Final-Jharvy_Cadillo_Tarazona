from typing import Dict, List, Optional
from services.service_a import database_user


def create_item(nombres: str, apellidos: str, edad: int) -> Dict[str, Optional[str]]:

    user_id = database_user.add_user(nombres, apellidos, edad)
    user = {
        "id": user_id,
        "nombre": nombres,
        "apellido": apellidos,
        "edad": edad
    }
    return user


def get_all_user() -> List[Dict[str, Optional[str]]]:
    try:
        users = database_user.list_users()
        return users
    except Exception as exc:
        print("Error al recuperar a los usuarios")
        return []
    
def delete_user(id: int):
    try:
        database_user.delete_user()
    except Exception as exc:
        print(f"Error al eliminar al usuario con id: {id}")