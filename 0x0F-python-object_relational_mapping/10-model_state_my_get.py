#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    name_to_search = argv[4]

    DB_URI = f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    engine = create_engine(DB_URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)\
        .filter(State.name == name_to_search)\
        .order_by(State.id)\
        .first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
