#!/usr/bin/python3

"""
    City model for db hbtn_0e_6_usa
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey("states.id"))
    state = relationship("State", backref="cities")

    def __init__(self, name):
        self.name = name
        self.state = state
