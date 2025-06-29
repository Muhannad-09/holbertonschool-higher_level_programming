#!/usr/bin/python3
"""Definition of State class and instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """State class mapped to the 'states' table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
