#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    DB_URI = f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    engine = create_engine(DB_URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    a_states = session.query(State)\
        .filter(State.name.contains('a'))\
        .order_by(State.id)\
        .all()

    if a_states:
        for state in a_states:
            print(f"{state.id}: {state.name}")

    session.close()
