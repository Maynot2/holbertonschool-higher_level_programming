#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    ca = State(name='California')
    sf = City(name='San Francisco')
    sf.state = ca

    session.add_all([ca, sf])

    session.commit()
    session.close()
