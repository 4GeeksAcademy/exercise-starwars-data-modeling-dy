import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_suscripcion = Column(DateTime(timezone=True), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    



class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=False)
    


class Create_Planet(Base):
    __tablename__ = 'create_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_create_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    create_planet = relationship(User, Planet)

class Create_Character(Base):
    __tablename__ = 'create_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    chracter_create_id = Column(Integer, ForeignKey('chracater.id'), nullable=False)
    create_character = relationship(User, Character)

class Create_Vehicle(Base):
    __tablename__ = 'create_vehicle'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicle_create_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    create_vehicle = relationship(User, Vehicle) 


class Favorito_Planet(Base):
    __tablename__ = 'favorito_planet'
    id = Column(Integer, primary_key=True)
    planet_favorito_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorito_planet = relationship(User, Planet)
    

class Favorito_Character(Base):
    __tablename__ = 'favorito_character'
    id = Column(Integer, primary_key=True)
    character_favorito_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorito_character = relationship(User, Character)

class Favorito_Vehicle(Base):
    __tablename__ = 'favorito_vehicle'
    id = Column(Integer, primary_key=True)
    vehicle_favorito_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorito_vehicle = relationship(User, Vehicle)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
