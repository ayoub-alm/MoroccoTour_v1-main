#!/usr/bin/python3
"""Mysql Database Module"""
from urllib.parse import quote
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.users import User
from models.places import Place
from models.regions import Region
from models.cities import City
from models.facilities import Facility
from models.reviews import Review
from models.categories import Category

classes = {
    'Region': Region,
    'City': City,
    'Place': Place,
    'Review': Review,
    'Facility': Facility,
    'User': User,
    'Category': Category
}

class DBStorage:
    """DB storage class definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Engine DB initialization"""
        user = 'root'
        pwd = quote('')
        host = 'localhost'
        db = 'morocco_tour_db'
        self.__engine = create_engine('mysql+pymysql://root:@localhost/morocco_tour_db', pool_pre_ping=True)

    def all(self, cls=None):
        """Load objects from DB
        Args:
            cls (class): Class name to be loaded
        """
        objs_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
        """Add obj to DB
        Args:
            obj: Object to add
        """
        self.__session.add(obj)

    def save(self):
        """Commit changes to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from DB
        Args:
            obj: Object to delete
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables on DB and initialize session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current session"""
        self.__session.remove()

    def get(self, cls, id):
        """Retrieve one object
        Args:
            cls (class): Class of object to retrieve
            id (string): ID of object to retrieve
        """
        if cls in classes.values():
            return self.__session.query(cls).filter_by(id=id).first()
        return None

    def count(self, cls=None):
        """Count number of objects in storage
        Args:
            cls (class): Class to count objects of (optional)
        """
        if cls in classes.values():
            return self.__session.query(cls).count()
        else:
            count = 0
            for clss in classes.values():
                count += self.__session.query(clss).count()
            return count
