'''Tests for the assignment endpoints'''

from fastapi import HTTPException
import datetime
import pytest
from ..main import add_assignment, get_assignment, delete_assignment
from models.assignment_model import AssignmentModel

# tests

@pytest.mark.asyncio
async def test_add_non_existent_assignment():
    '''Test adding a non-existent (new) assignment to the database'''
    assignment = AssignmentModel(
        assignment_id=3,
        title="Descargar PSeInt",
        description="Ahora sí algo suave jsjs.",
        assignment_date="2025-04-05T10:10:10",
        deadline="2025-04-07T00:00:00",
        class_id=20
    )

    expected_result = {
        "msg": "Assignment added successfully.",
        "id": f'{assignment.assignment_id}'
    }

    try:
        await delete_assignment(assignment.assignment_id)
    except:
        pass

    result = ""

    try:
        result = await add_assignment(assignment)
    except Exception as e:
        result = e

    assert expected_result == result
