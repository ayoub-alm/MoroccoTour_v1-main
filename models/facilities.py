#!/usr/bin/python3
""" facilitiy class module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.places import place_facility


class Facility(BaseModel, Base):
    """facility class definition"""
    __tablename__ = 'facilities'


    name = Column('name', String(128), nullable=False, default="")