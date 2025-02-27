from fastapi import HTTPException
import datetime
import pytest
from ..main_new import add_user, get_user, delete_user
from ..models.user_model import UserModel

# tests

@pytest.mark.asyncio
async def test_add_non_existent_user():
    '''Test adding a non-existent (new) user to the database'''
    user = UserModel(
        user_id=1,
        first_name="Jose",
        middle_name="Luis",
        last_name="Perez",
        second_last_name="Gomez",
        email="jpergomez@example.com",
        password="password123",
        sign_up_date="2021-10-10T10:10:10",
        role_id=1
    )

    expected_result = {
        "msg": "User added successfully.",
        "id": f'{user.user_id}'
    }

    try:
        await delete_user(user.user_id)
    except:
        pass

    result = ""

    try:
        result = await add_user(user)
    except Exception as e:
        result = e

    assert expected_result == result

@pytest.mark.asyncio
async def test_add_existing_user():
    '''Test adding an existing user to the database'''
    user = UserModel(
        user_id=1,
        first_name="Jose",
        middle_name="Luis",
        last_name="Perez",
        second_last_name="Gomez",
        email="jpergomez@example.com",
        password="password123",
        sign_up_date="2021-10-10T10:10:10",
        role_id=1
    )

    expected_result = HTTPException(status_code=409, detail="User already exists. {'_id': 1, 'first_name': 'Jose', 'middle_name': 'Luis', 'last_name': 'Perez', 'second_last_name': 'Gomez', 'email': 'jpergomez@example.com', 'password': 'password123', 'sign_up_date': datetime.datetime(2021, 10, 10, 10, 10, 10), 'role_id': 1}")

    try:
        await add_user(user)
    except:
        pass

    result = ""

    try:
        result = await add_user(user)
    except Exception as e:
        result = e

    assert result.status_code == expected_result.status_code
    assert result.detail == expected_result.detail

@pytest.mark.asyncio
async def test_get_existing_user():
    '''Test getting an existing user from the database'''
    user_id = 1

    try:
        await add_user(UserModel(user_id=user_id))
    except:
        pass

    expected_result = {'_id': 1, 'first_name': 'Jose', 'middle_name': 'Luis', 'last_name': 'Perez', 'second_last_name': 'Gomez', 'email': 'jpergomez@example.com', 'password': 'password123', 'sign_up_date': datetime.datetime(2021, 10, 10, 10, 10, 10), 'role_id': 1}

    result = ""

    try:
        result = await get_user(user_id)
    except Exception as e:
        result = e

    assert expected_result == result

@pytest.mark.asyncio
async def test_remove_existing_user():
    '''Test removing an existing user from the database'''
    user_id = 1

    expected_result = {"msg": "User deleted succesfully.", "id": user_id}

    try:
        await add_user(UserModel(user_id=user_id))
    except:
        pass

    result = ""

    try:
        result = await delete_user(user_id)
    except Exception as e:
        result = e

    assert expected_result == result

@pytest.mark.asyncio
async def test_remove_non_existent_user():
    '''Test removing a non-existent user from the database'''
    user_id = 1

    expected_result = HTTPException(status_code=404, detail="User not found.")

    try:
        await delete_user(user_id)
    except:
        pass

    result = ""

    try:
        result = await delete_user(user_id)
    except Exception as e:
        result = e

    assert result.status_code == expected_result.status_code
    assert result.detail == expected_result.detail
