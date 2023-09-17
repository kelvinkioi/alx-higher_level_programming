#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
import MySQLdb
import sqlalchemy
from model_state import Base, State
from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    try:
        engine = create_engine(
           'mysql+mysqldb://{}:{}@localhost:3306/{}'
           .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
        )
    except Exception as e:
        print(e)
        exit()

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    for i in ses.query(State).order_by(State.id).all():
        print(f"{i.id}: {i.name}")
    ses.close()
