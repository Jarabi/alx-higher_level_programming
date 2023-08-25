#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
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

    california = session.query(State)\
        .filter(State.name == "California")\
        .first()

    if california is None:
        state = State(name="California")
        city = City(name="San Francisco", state=state)
        session.add(city)
        session.flush()
        session.commit()
