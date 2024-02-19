#!/usr/bin/python3

from datetime import datetime
import models
import uuid


class BaseModel:
    """
    BaseModel class enables creation and instances manager.
    """
    def __init__(self, *args, **kwargs):
        '''
        Docs
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key == 'id':
                    self.id = str(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        '''
        Docs
        '''
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def __str__(self):
        '''
        returns string representatioon of instances
        '''
        class_name = type(self).__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    

    def to_dict(self) -> dict:
        """
        Return a dictionary of every instance attributes.
        """
        sect = ['name', 'my_number']
        dictionary = {key: value for key, value in self.__dict__.items() if key not in sect}
        dictionary['__class__'] = self.__class__.__name__

        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()

        return dictionary
    
