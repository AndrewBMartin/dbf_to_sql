DBF to SQL

Dumps a DBF file to a SQL table using SQLAlchemy.

Default is Sqlite3, but you should be able to substitute 
in your favourite RDS by changing the database uri in the
script.

Dependencies:
SQLAlchemy
dbf

Usage:
To be used interactively or in a script.

from dbf_to_sql import dbf_to_sql as dts

dbf_file = "mydbf.dbf"

Session = dts(dbf_file)

session = Session()

# Perform queries on your session in SQLAlchemy style

