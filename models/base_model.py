#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from datetime import datetime
import models
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models
    Attributes:
        id (sqlalchemy String): id for BaseModel
        created_at (sqlachemy DateTime): creation date and time
        updated_at (sqlalchemy DateTime): update date and time
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model
        Args:
            *args (any): This variable is unused
            *kwargs (dict): attributes with key/value pairs
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        _dict = self.__dict__.copy()
        _dict.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, _dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert BaseModel instance into dict format
        has key/value pairs representing class names
        """
        _dict = self.__dict__.copy()
        _dict["__class__"] = str(type(self).__name__)
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        _dict.pop("_sa_instance_state", None)
        return _dict

    def delete(self):
        """Deletes the current instance from the database"""
        models.storage.delete(self)