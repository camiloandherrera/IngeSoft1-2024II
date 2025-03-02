'''Base router class that provides common CRUD operations in API'''

from fastapi import HTTPException
from abc import ABC

# mvcs (view/api)

class BaseRouter(ABC):
    '''Base endpoint router class that provides common CRUD operations'''

    service = None

    # Base CRUD endpoints

    async def add(self, entity: dict):
        '''Adds an entity to the database'''
        result = self.service.add(entity)

        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    async def get(self, entity_id: int):
        '''Gets an entity from the database'''
        result = self.service.get(entity_id)

        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result

    async def update(self, entity_id: int, updates: dict):
        '''Updates an entity in the database'''
        result = self.service.update(entity_id, updates)

        if "error" in result:
            raise HTTPException(status_code=403, detail=result["error"])
        return result

    async def delete(self, entity_id: int):
        '''Deletes an entity from the database'''
        result = self.service.delete(entity_id)

        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result

    async def get_all(self):
        '''Gets all entities from the database; early development for
        retrieval testing purposes'''
        result = self.service.get_all()

        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
