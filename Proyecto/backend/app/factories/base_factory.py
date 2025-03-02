'''Base factory method class for concrete factory methods'''

from abc import ABC, abstractmethod

# factory method

class BaseFactory(ABC):
    '''Base factory method class'''
    @abstractmethod
    def create(self, entity_data: dict):
        '''Abstract factory method'''
        pass
