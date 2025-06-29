#!/usr/bin/python3
"""Fetch all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql_username> "
              "<mysql_password> <database_name>")
        sys.exit(1)

    # Create engine and session
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities and states
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Display results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
