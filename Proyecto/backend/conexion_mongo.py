"""MongoDB connection"""

from pymongo import MongoClient

# Conexión a MongoDB
MONGO_URI = "mongodb+srv://Administrador:PttuZVjgwQeAckM5@cluster0.kqodv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
cliente = MongoClient(MONGO_URI)

# Selcets database and collection
db = cliente["Base_de_datos_seguimiento_proyectos"]


def agregar_usuario(
    cedula: int, nombre: str, email: str, edad: int, activo: bool, tipo_de_usuario: str
):
    """Document of the user to add"""
    coleccion = db["usuarios"]
    usuario_existente = coleccion.find_one({"_id": cedula})
    if usuario_existente:
        return {"error": f"El usuario ya existe {usuario_existente}"}
    else:
        nuevo_usuario = {
            "_id": cedula,
            "nombre": nombre,
            "email": email,
            "edad": edad,
            "activo": activo,
            "tipo_de_usuario": tipo_de_usuario,
        }
        try:
            resultado = coleccion.insert_one(nuevo_usuario)
            return {"mensaje": "Usuario agregado", "id": str(resultado.inserted_id)}
        except Exception as e:
            return {"error": f"Error al conectar o insertar: {e}"}


def eliminar_usuario(cedula: int):
    """Deletes a user"""
    coleccion = db["usuarios"]
    usuario_existente = coleccion.find_one({"_id": cedula})
    if usuario_existente:
        try:
            resultado = coleccion.delete_one({"_id": cedula})
            return {"mensaje": "Usuario eliminado", "id": cedula}
        except Exception as e:
            return {"error": f"Error al conectar o eleiminar: {e}"}
    else:
        return {"error": f"El usuario NO existe {usuario_existente}"}
