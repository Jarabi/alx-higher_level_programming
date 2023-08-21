#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
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

    result = session.query(State.name, City.id, City.name)\
        .join(City, City.state_id == State.id)\
        .order_by(City.id)\
        .all()

    for s_name, c_id, c_name in result:
        print(f"{s_name}: ({c_id}) {c_name}")

    session.close()
