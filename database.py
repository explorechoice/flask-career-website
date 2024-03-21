#https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples
import sqlalchemy
from sqlalchemy import create_engine, text
import os

version = sqlalchemy.__version__
print(version)

# we need to connect to our MySQL database hosted on 
# https://console.aiven.io/account/a49f42ba3bcb/project/sharma-4204/services/mysql-vaikuntha/overview
# to connect database we need to create an engine

# Since SQLAlchemy works with many different database types, you'll need an underlying library, called a database driver, to connect to your database and communicate with it. You don't have to use this driver directly, because as long as SQLAlchemy has the correct driver, it will automatically use it for everything. The Python MySQL Connector is used as the driver in this tutorial, but other good ones are PyMySQL and MySQLdb.

# You'll need to install your driver with pip.

connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(connection_string, echo=True)

def load_openings_from_db():
  openings = []
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs"))
    result_all = result.all()
    for row in result_all:
      row_as_dict = row._mapping
      print(row_as_dict)
      openings.append(row_as_dict)
  return openings

def load_openings():
  openings = []
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs"))
    result_all = result.all()
    for row in result_all:
      row_as_dict = row._mapping
      print(f'row_as_dict: {(row_as_dict)}')
      openings.append((row_as_dict))
  return openings