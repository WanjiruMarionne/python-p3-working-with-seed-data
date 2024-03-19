#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
    session.add(botw)
    session.commit()

    import ipdb; ipdb.set_trace()