#!/usr/bin/python3
"""class User Module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User Class definition"""
    __tablename__ = "users"

    first_name = Column("first_name", String(128), nullable=False)
    last_name = Column("last_name", String(128), nullable=False)
    email = Column("email", String(128), nullable=False)
    password = Column("password", String(128), nullable=False)
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
