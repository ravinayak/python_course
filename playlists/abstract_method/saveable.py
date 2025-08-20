from abc import ABCMeta, abstractmethod
from playlists.abstract_method.database import Database

class Saveable(metaclass=ABCMeta):
    def save(user):
        Database.save(user)
        
    @abstractmethod
    def to_dict(user):
        pass
