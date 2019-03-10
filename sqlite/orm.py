import json
import logging

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import update

Base = automap_base()

logger = logging.getLogger('orm')


class Band(Base):  # raw data from MA
    __tablename__ = "band"

    name = Column(String)
    themes = Column(String)
    style = Column(String)
    city = Column(String)
    region = Column(String)
    country = Column(String)
    metal_archives_id = Column(String, primary_key=True)


class LyricalThemes(Base):
    __tablename__ = "lyrical_themes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lyrical_theme = Column(String)
    metal_archives_id = Column(
        String,
        ForeignKey("band.metal_archives_id"))  # link to metal archives id
    band = relationship("Band", backref=backref('metal_archives_id', uselist=False),remote_side=Band.metal_archives_id)


class Genres(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    genre = Column(String)
    metal_archives_id = Column(
        String, ForeignKey("band.metal_archives_id"))  # link to ma id
    band = relationship("Band", backref=backref('metal_archives_id', uselist=False), remote_side=Band.metal_archives_id)


def create_all():
    engine = create_engine('sqlite:///metal.db')
    session = sessionmaker()
    session.configure(bind=engine)
    Base.prepare()
    Base.metadata.create_all(engine)
    logging.debug("tables created")


def insert_from_json(bandlist):
    engine = create_engine('sqlite:///metal.db')
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    for idx, band in enumerate(bandlist):
        ma_id = band.get("metalarchives_id", "")
        b = Band(
            name=band.get("name", ""),
            themes=band.get("lyrical_themes", ""),
            style=band.get("style", ""),
            city=band.get("city", ""),
            region=band.get("region", ""),
            country=band.get("country", ""),
            metal_archives_id=ma_id)
        s.add(b)
        for genre in band.get("genres"):
            g = Genres(genre=genre, metal_archives_id=ma_id)
            s.add(g)
        for theme in band.get("themes"):
            t = LyricalThemes(lyrical_theme=theme, metal_archives_id=ma_id)
            s.add(t)
        logger.debug(f'{band.get("name")} added')
    logger.debug(f'committing bandlist')
    s.commit()
    logger.debug(f'total bands added: {s.query(Band).count()}')
