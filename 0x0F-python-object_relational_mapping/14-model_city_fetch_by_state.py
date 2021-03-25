#!/usr/bin/python3
"""
    Simple query all to db
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                            usr,
                                                            pwd,
                                                            db,
                                                            pool_pre_ping=True
                                                        ))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State).all()

    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))

    session.close()
