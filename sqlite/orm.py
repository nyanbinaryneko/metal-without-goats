import json
import logging

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Band(Base): # raw data from MA
    __tablename__="bands" 

    id = Column(Integer, primary_key=True) # auto increment id
    name = Column(String)
    themes = Column(String)
    style = Column(String)
    city = Column(String)
    region = Column(String)
    country = Column(String)
    metal_archives_id = Column(String, primary_key=True)

class LyricalThemes(Base):
    __tablename__ = "lyrical_themes"

    id = Column(Integer, primary_key=True)
    lyrical_theme = Column(String)
    metal_archives_id = Column(String, ForeignKey("bands.metal_archives_id")) # link to metal archives id

class Genres(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    genre = Column(String)
    metal_archives_id = Column(String, ForeignKey("bands.metal_archives_id")) # link to ma id

def create_all():
    engine = create_engine('sqlite:///metal.db')
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
