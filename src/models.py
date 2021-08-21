import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__= 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))

class People(Base):
    __tablename__= 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250))
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    homeworld = relationship(Planet)
    mass = Column(String(250))
    skin_color = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))

class Vehicles(Base):
    __tablename__= 'vehicles'
    id Pk int
    name = Column(String(250))
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    length = Column(String(250))
    cost_in_credits = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')