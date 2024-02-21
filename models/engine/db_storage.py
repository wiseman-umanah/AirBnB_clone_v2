#!/usr/bin/python3
"""The DataBase Storage system with mysql"""
from sqlalchemy import create_engine, delete
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.user import User
from models.state import State


class DBStorage:
    """Creates and query database engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.user = getenv('HBNB_MYSQL_USER')
        self.pwd = getenv('HBNB_MYSQL_PWD')
        self.host = getenv('HBNB_MYSQL_HOST')
        self.dbname = getenv('HBNB_MYSQL_DB')
        self.env = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
            self.user, self.pwd, self.host, 3306, self.dbname),
            pool_pre_ping=True)
        if self.env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """List all instances of a class or all classes"""
        classes = {
                    'State': State, 'City': City,
                    'User' : User, 'Place': Place,
                    'Amenity': Amenity, 'Review': Review
                  }
        instances = {}
        for clsId in classes:
            if cls is None:
                data = self.__session.query(classes[clsId]).all()
            else:
                data = self.__session.query(cls).all()
            for ins in data:
                keyId = f"{ins.__class__.__name__}.{ins.id}"
                instances[keyId] = ins
        return (instances)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to database"""
        self.__session.commit()

    def reload(self):
        """reloads engine for setup"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def delete(self, obj=None):
        """Deletes an object from the database"""
        classes = {"City": City}
        if obj is not None:
            table, id = obj.split(".")
            model = self.__session.query(classes[table]).filter(classes[table].id == id).first()
            if model:
                self.__session.delete(model)
                self.save()
            else:
                raise KeyError
