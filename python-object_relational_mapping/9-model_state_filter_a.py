#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to the DB and display states with 'a' in their name."""
    if len(sys.argv) != 4:
        sys.exit(1)

    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Use contains() safe filter, wrapped into multiple lines for PEP 8
    states = (
        session.query(State)
        .filter(State.name.contains('a'))
        .order_by(State.id)
        .all()
    )

    for st in states:
        print(f"{st.id}: {st.name}")

    session.close()


if __name__ == "__main__":
    main()
