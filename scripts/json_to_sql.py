import json_helper
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
import logging

# creates tables for metal archives db
DB_URI = 'sqlite:///metal.db'

logging.basicConfig(filename="db_log.log",filemode="w+",level=logging.INFO)

def create_tables():
    engine = create_engine(DB_URI)
    metadata = MetaData(engine)

    #tables
    bands = Table('bands', metadata,
                Column('name', String),
                Column('themes', String),
                Column("styles", String),
                Column('city', String),
                Column('region', String),
                Column('country', String),
                Column('metal_archives_id', String, primary_key=True))

    themes = Table('themes', metadata,
                Column('theme', String),
                Column('metal_archives_id', String))

    genres = Table('genres', metadata,
                Column('genre', String),
                Column('metal_archives_id', String))

    metadata.create_all()

    for _t in metadata.tables:
        print("Table: ", _t)
    return "tables created"

def insert_band(band, conn, meta):
    table = meta.tables['bands']
    ins = table.insert().values(
                        name=band.get('name'),
                        themes=band.get('lyrical_themes'),
                        styles=band.get("style"),
                        city=band.get('city'),
                        region=band.get('region'),
                        country=band.get('country'),
                        metal_archives_id=band.get('metalarchives_id')
                        )
    conn.execute(ins)
    return "inserted " + band.get("name") 

def insert_genre(conn, meta, archive_id, genre="None"):
    logging.info("genre: " + genre)
    table = meta.tables['genres']
    if genre == "None":
        ins = table.insert().values(metal_archives_id=archive_id)
    else:
        ins = table.insert().values(metal_archives_id=archive_id, genre=genre)
    conn.execute(ins)
    return "inserted genre for " + archive_id

def insert_theme(conn, meta, archive_id, theme="None"):
    logging.info("theme: " + theme)
    table = meta.tables['themes']
    if theme == None:
        ins = table.insert().values(metal_archives_id=archive_id)
    else:
        ins = table.insert().values(metal_archives_id=archive_id, theme=theme)
    conn.execute(ins)
    return "inserted theme for " + archive_id

def main():
    logging.info(create_tables())

    # load list of bands into memory because I can't find a streaming library that works.
    bands = json_helper.load_list('./json/test-fix.json')
    engine = create_engine(DB_URI)
    conn = engine.connect()
    meta = MetaData(engine, reflect=True)
    
    # iterate through list:
    logging.info("iterating through list")
    for band in bands:
        logging.info("band: " + band.get('name'))
        #
        trans = conn.begin()
        logging.info(insert_band(band, conn, meta))
        trans.commit()
    """ archive_id = band.get('metalarchives_id')
        genres = band.get("genres")
        themes = band.get("themes")
        if len(genres) < 1:
            insert_theme(conn, meta, archive_id)
            #trans.commit()
        if len(themes) < 1:
            insert_theme(conn, meta, archive_id)
            #trans.commit()
        for genre in genres:
            insert_genre(conn, meta, archive_id, genre)
            #trans.commit()
        for theme in themes:
            insert_theme(conn, meta, archive_id, theme)
            #trans.commit() """
    conn.close()                
        #print(band.get('genres'))
    
    pass

if __name__ == '__main__':
    main()