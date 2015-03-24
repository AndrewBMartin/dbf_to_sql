from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from sqlalchemy.orm import mapper, create_session
import csv
import dbf


def dump_dbf(dbf_file):
    """
    Read through a dbf file
    and create an in memory sqlite database
    to store the records.
    """

    engine = create_engine('sqlite://') # memory-only database

    table = None
    metadata = MetaData(bind=engine)

    dbf_table = dbf.Table(dbf_file)
    dbf_table.open()
    field_names = dbf_table.field_names

    for row in dbf_table:
        if table is None:
            # create the table
            table = Table(dbf_file, metadata, 
                Column('id', Integer, primary_key=True),
                *(Column(rowname, String()) for rowname in 
                  field_names))
            table.create()
        # insert data into the table
        row = dict(zip(field_names, [str(r).strip() for r in row]))
        table.insert().values(**row).execute()

    class dbfTable(object): pass
    mapper(dbfTable, table)

    Session = create_session(bind=engine, autocommit=False, autoflush=True)
    return Session
