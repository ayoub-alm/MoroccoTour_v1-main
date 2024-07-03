#!/usr/bin/python3
"""class Region Module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Region(BaseModel, Base):
    """Region Class definition"""
    __tablename__ = "regions"

    name = Column("name", String(128), nullable=False)
    cities = relationship("City", backref="region", cascade="delete")
