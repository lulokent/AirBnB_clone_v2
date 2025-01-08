#!/usr/bin/python3
""" Database storage setup"""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from os import getenv


class DBStorage:
    """ class represeting database storage
    Attributes:
        __engine,
        __session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Creates the database engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Queries all objects in the session"""
        _objDict = {}

        if cls == None:
            _objList = self.__session.query(State).all()
            _objList.extend(self.__session.query(City).all())
            _objList.extend(self.__session.query(User).all())
            _objList.extend(self.__session.query(Place).all())
            _objList.extend(self.__session.query(Review).all())
            _objList.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            _objList = self.__session.query(cls).all()

        for obj in _objList:
            _key = "{}.{}".format(type(obj).__name__, obj.id)
            _objDict[_key] = obj

        return _objDict

    def new(self, obj):
        """Adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Saves changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes object from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in database"""
        Base.metadata.create_all(self.__engine)
        _newSession = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(_newSession)
        self.__session = Session()

    def close(self):
        """Closes session"""
        self.__session.close()