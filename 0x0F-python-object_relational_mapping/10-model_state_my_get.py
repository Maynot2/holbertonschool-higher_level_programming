#!/usr/bin/python3
"""
    Simple query all to db
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                            usr,
                                                            pwd,
                                                            db,
                                                            pool_pre_ping=True
                                                        ))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=state_name).first()

    if state:
        print('{}'.format(state.id))
    else:
        print('Not found')
