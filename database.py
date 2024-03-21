#https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples
import json
import os
from datetime import date, datetime

import sqlalchemy
from sqlalchemy import create_engine, text

version = sqlalchemy.__version__

# we need to connect to our MySQL database hosted on 
# https://console.aiven.io/account/a49f42ba3bcb/project/sharma-4204/services/mysql-vaikuntha/overview
# to connect database we need to create an engine

# Since SQLAlchemy works with many different database types, you'll need an underlying library, called a database driver, to connect to your database and communicate with it. You don't have to use this driver directly, because as long as SQLAlchemy has the correct driver, it will automatically use it for everything. The Python MySQL Connector is used as the driver in this tutorial, but other good ones are PyMySQL and MySQLdb.

# You'll need to install your driver with pip.

connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(connection_string, echo=True)


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def load_openings_from_db():
  openings = []
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs"))
    result_all = result.all()
    for row in result_all:
      row_as_dict = row._mapping
      openings.append(row_as_dict)
  return openings

def load_openings_by_id(id):
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs WHERE id = :val"), parameters=dict(val=id))
    result_all = result.all()[0]
    print(result_all)
    if len(result_all) != 0:
      return dict(result_all._mapping)
    else:
      return None

def load_openings():
  openings = []
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs"))
    result_all = result.all()
    for row in result_all:
      row_as_dict = dict(row._mapping)
      print(f'row_mapping: {row_as_dict}')
      json_r = json.dumps(row_as_dict, default=json_serial)
      print(f'dump data: {row_as_dict}')
      load_r = json.loads(json_r)
      print(f'row_as_dict: {(load_r)}')
      openings.append((load_r))
  return openings