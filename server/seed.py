#!/usr/bin/env python3

# Standard library imports
from datetime import datetime

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User

if __name__ == '__main__':
    fake = Faker()

    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create example user
        user = User(email="paigeberliner@gmail.com", first_name="Paige", last_name="Berliner", created_at=datetime.now())

        
        db.session.add(user)
        db.session.commit()


        print("Seeding complete.")