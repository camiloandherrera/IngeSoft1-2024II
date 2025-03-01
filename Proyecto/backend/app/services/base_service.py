'''Base service class that provides common CRUD operations in services'''

from abc import ABC

# mvc (controller/service)

class BaseService(ABC):
    '''Base service class that provides common CRUD operations'''
    repo = None

    def add(self, entity, entity_name: str):
        '''Adds an entity to the database'''
        exists = self.repo.get(entity.entity_id)
        if exists:
            return {"error": f"{entity_name} already exists. {exists}"}
        else:
            try:
                result = self.repo.add(entity)
                return {"msg": f"{entity_name} added successfully.", "_id": str(result.inserted_id)}
            except Exception as e:
                return {"error": f"Connection error or insert error: {e}"}

    def get(self, entity_id: int, entity_name: str):
        '''Gets an entity from the database'''
        exists = self.repo.get(entity_id)
        if not exists:
            return {"error": f"{entity_name} not found."}
        else:
            try:
                return exists
            except Exception as e:
                return {"error": f"Connection error or retrieve error: {e}"}

    def update(self, entity_id: int, updates: dict, entity_name: str):
        '''Updates an entity in the database'''
        exists = self.repo.get(entity_id)
        if not exists:
            return {"error": f"{entity_name} not found."}
        else:
            try:
                self.repo.update(entity_id, updates)
                return {"msg": f"{entity_name} updated successfully.", "entity_id": entity_id}
            except Exception as e:
                return {"error": f"Connection error or update error: {e}"}


    def delete(self, entity_id: int, entity_name: str):
        '''Deletes an entity from the database'''
        exists = self.repo.get(entity_id)
        if not exists:
            return {"error": f"{entity_name} not found."}
        else:
            try:
                self.repo.delete(entity_id, entity_name)
                return {"msg": f"{entity_name} deleted succesfully.", "entity_id": entity_id}
            except Exception as e:
                return {"error": f"Connection error or delete error: {e}"}


    def get_all(self):
        '''Gets all the entities from the database; early development for
        retrieval testing purposes'''
        try:
            retrieved_entities_cursor = self.repo.get_all()
            entities = list(retrieved_entities_cursor)
            return entities
        except Exception as e:
            return {"error": f"Connection error or retrieve error: {e}"}
