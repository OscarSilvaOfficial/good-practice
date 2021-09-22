from abc import abstractclassmethod
from api.sqlalchemy import db

class BaseModel(db.Model):
    
    @abstractclassmethod 
    def serialize(self):
        pass

    def all(self):
        return self.query.all()