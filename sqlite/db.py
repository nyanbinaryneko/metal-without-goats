import json
import logging

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey

class SqliteDB:

    def __init__(self):
        self.db_uri = 'sqlite:///metal.db'
        self.engine = create_engine(self.db_uri)
        self.metadata = MetaData(self.engine)

    def create_tables(self):
        
        # tables
        bands = Table(
            'bands',
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('themes', String),
            Column('city', String),
            Column('region', String),
            Column('country', String),
            Column('metal_archives_id', String, primary_key=True),
            sqlite_autoincrement=True)

        themes = Table('themes',self.metadata, Column('theme', String),
                    Column('metal_archives_id', String))

        genres = Table('genres',self.metadata, Column('genre', String),
                    Column('metal_archives_id', String))

        self.metadata.create_all()

        for _t in self.metadata.tables:
            logging.info(f'{_t} created.')

