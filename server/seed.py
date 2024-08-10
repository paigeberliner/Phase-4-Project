#!/usr/bin/env python3

# Standard library imports
from datetime import datetime

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, AvailableClass, ClaimedClass

if __name__ == '__main__':
    fake = Faker()

    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create example user
        user = User(email="paigeberliner@gmail.com", first_name="Paige", last_name="Berliner", created_at=datetime.now())

        # Create example available class
        available_class = AvailableClass(
            class_name="Yoga Sculpt",
            studio="CorePower",
            class_time=datetime(2024, 8, 10, 19, 0),
            class_duration=60,
            address="Mezzanine Level, 24 W 40th St, New York, NY 10018",
            user_id=user.id  # Make sure the user exists when adding this
        )

        # Add the data to the session
        db.session.add(user)
        db.session.add(available_class)
        db.session.commit()

        # Create example claimed class
        claimed_class = ClaimedClass(
            available_class_id=available_class.id,
            claimed_time=datetime.now(),
            user_id=user.id
        )

        # Add the claimed class to the session
        db.session.add(claimed_class)
        db.session.commit()

        print("Seeding complete.")
