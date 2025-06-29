#!/usr/bin/python3
"""Print the State object with the name passed as argument from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 5:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()


if __name__ == "__main__":
    main()
