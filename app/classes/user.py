from os import urandom 
from bson import ObjectId

from app import db

class User:
    def __init__(self, id, name, number):
        self.id = str(id)
        self.name = name
        self.number = number

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(dictionary):
        return User(str(dictionary.get("_id")),
                    dictionary.get("name"),
                    dictionary.get("number")
        )
    
    @staticmethod
    def get_users():
        return [User.from_dict(user) for user in db.users.find({})]
    
    @staticmethod
    def get_user_by_id(id):
        return User.from_dict(db.users.find_one({'_id': ObjectId(id)}))
    
    @staticmethod
    def delete_user_by_id(id):
        db.users.remove({'_id': ObjectId(id)})

    def __repr__(self):
        return f"User('{str(self.id)}', '{self.name}', '{self.number}')"