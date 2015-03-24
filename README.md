# DBF to SQL

Dumps a DBF file to a SQL table using SQLAlchemy.

Default is Sqlite3, but you should be able to substitute 
in your favourite RDS by changing the database uri in the
script.

Dependencies:
SQLAlchemy
dbf

Usage:
To be used interactively or in a script.

>> from dbf_to_sql import dbf_to_sql as dts

>> dbf_file = "mydbf.dbf"

>> table_obj = dts(dbf_file)

>> table_obj
{"session": session,
 "engine": engine,
 "metadata": metadata,
 "field_names": field_names}

>> session = table_obj.session

Perform queries on your session in SQLAlchemy style

