#!/usr/bin/python3
"""Base Model that defines all common attributes
"""
import uuid
from datetime import datetime as dt
import models
import datetime


class BaseModel:
    """Module blueprint of the common attributes
    """

    def __init__(self, *args, **kwargs):
        """Instantiating base model common variables

            Args:
                id(str): a unique string id for created instance
                created_at(datetime): date when instance is created
                updated_at(datetime): date when instance is modified
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        setattr(self,
                                key,
                                dt.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                                )
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Method used to display output in a human readable string
            representation

            Return:
                returns formatted output with class name, id and dict
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method to update the public instance attribute with current datetime
        """
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """Function to return a dictionary containing all keys/values of
            __dict__ of the instance

            Return:
                returns a dictionary of class attributes
        """
        attrs = self.__dict__.copy()
        attrs['created_at'] = self.created_at.isoformat()
        attrs['updated_at'] = self.updated_at.isoformat()
        attrs['__class__'] = self.__class__.__name__
        return attrs
