#!/usr/bin/python3

"""
    State model for db hbtn_0e_6_usa
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    def __init__(self, name):
        self.name = name
