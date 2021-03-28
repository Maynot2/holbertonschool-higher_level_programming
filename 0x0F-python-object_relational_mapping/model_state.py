#!/usr/bin/python3

"""
    State model for db hbtn_0e_6_usa
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State model"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        """Constructor for State instances"""
        self.name = name
