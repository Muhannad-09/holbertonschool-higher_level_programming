#!/usr/bin/python3
"""State model with relationship to City"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete", passive_deletes=True)

