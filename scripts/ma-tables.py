import json
import logging

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey


def create_tables():
    db_uri = 'sqlite:///metal.db'
    engine = create_engine(db_uri)
    metadata = MetaData(engine)

    #tables
    bands = Table(
        'bands',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('themes', String),
        Column('city', String),
        Column('region', String),
        Column('country', String),
        Column('metal_archives_id', String, primary_key=True),
        sqlite_autoincrement=True)

    themes = Table('themes', metadata, Column('theme', String),
                   Column('metal_archives_id', String))

    genres = Table('genres', metadata, Column('genre', String),
                   Column('metal_archives_id', String))

    metadata.create_all()

    for _t in metadata.tables:
        logging.info(f'{_t} created.')


if __name__ == "__main__":
    create_tables()
