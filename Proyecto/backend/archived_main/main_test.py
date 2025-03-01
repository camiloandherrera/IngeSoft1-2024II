from fastapi import HTTPException
import pytest
from . import crear_usuario, delete_user, Usuario


@pytest.mark.asyncio
async def test_crear_usuario_NO_existente():
    cedula = 1
    nombre = "Jose"
    email = "Jose@gmail.com"
    edad = 30
    activo = True
    tipo_de_usuario = "administrador"

    usuario = Usuario(
        cedula=cedula,
        nombre=nombre,
        email=email,
        edad=edad,
        activo=activo,
        tipo_de_usuario=tipo_de_usuario
    )

    resultado_esperado = {
        "mensaje": "Usuario agregado",
        "id": f'{cedula}'
    }

    try:
        await delete_user(cedula)
    except:
        pass

    resultado = ""

    try:
        resultado = await crear_usuario(usuario)
    except Exception as e:
        resultado = e

    assert resultado_esperado == resultado

@pytest.mark.asyncio
async def test_crear_usuario_ya_existente():
    cedula = 1
    nombre = "Jose"
    email = "Jose@gmail.com"
    edad = 30
    activo = True
    tipo_de_usuario = "administrador"

    usuario = Usuario(
        cedula=cedula,
        nombre=nombre,
        email=email,
        edad=edad,
        activo=activo,
        tipo_de_usuario=tipo_de_usuario
    )

    resultado_esperado = HTTPException(status_code=409, detail="El usuario ya existe {'_id': 1, 'nombre': 'Jose', 'email': 'Jose@gmail.com', 'edad': 30, 'activo': True, 'tipo_de_usuario': 'administrador'}")

    try:
        await crear_usuario(usuario)
    except:
        pass

    resultado = ""

    try:
        resultado = await crear_usuario(usuario)
    except Exception as e:
        resultado = e

    assert resultado.status_code == resultado_esperado.status_code
    assert resultado.detail == resultado_esperado.detail

@pytest.mark.asyncio
async def test_eliminar_usuario_ya_existente():
    cedula = 1

    resultado_esperado = {"mensaje": "Usuario eliminado", "id": cedula}

    try:
        await crear_usuario(Usuario(cedula=cedula))
    except:
        pass

    resultado = ""

    try:
        resultado = await delete_user(cedula)
    except Exception as e:
        resultado = e

    assert resultado== resultado_esperado

@pytest.mark.asyncio
async def test_eliminar_usuario_NO_existente():
    cedula = 1

    resultado_esperado = HTTPException(status_code=404, detail="El usuario NO existe None")

    try:
        await delete_user(cedula)
    except:
        pass

    resultado = ""

    try:
        resultado = await delete_user(cedula)
    except Exception as e:
        resultado = e

    assert resultado.status_code == resultado_esperado.status_code
    assert resultado.detail == resultado_esperado.detail
