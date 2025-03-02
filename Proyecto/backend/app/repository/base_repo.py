'''Base repository class that provides common CRUD operations in respositories'''

from models.base_entity_model import BaseEntityModel

from abc import ABC

# repository

class BaseRepository(ABC):
    '''Provides common CRUD operations'''
    collection = None

    def add(self, entity: BaseEntityModel):
        '''Adds an entity to the database'''
        entity['_id'] = entity.pop('entity_id')  # Set entity_id as _id
        return self.collection.insert_one(entity)

    def get(self, entity_id: int):
        '''Gets an entity from the database'''
        return self.collection.find_one({"_id": entity_id})

    def update(self, entity_id: int, updates: dict):
        '''Updates an entity in the database'''
        return self.collection.update_one({"_id": entity_id}, {"$set": updates})

    def delete(self, entity_id: int):
        '''Deletes an entity from the database'''
        return self.collection.delete_one({"_id": entity_id})

    def get_all(self):
        '''Gets all entities from the database; early development for
        retrieval testing purposes'''
        return self.collection.find()
