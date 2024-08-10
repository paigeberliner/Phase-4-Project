#!/usr/bin/env python3

# Standard library imports
from datetime import datetime

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, WorkoutClass

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

        #Create an example workout class 
        class_date = datetime.strptime('2024-08-10', '%Y-%m-%d')  # Format YYYY-MM-DD
        class_time = datetime.strptime('19:00:00', '%H:%M:%S').time()  # 7 PM in 24-hour format

        workoutclass = WorkoutClass(
            studio_name="CorePower",
            studio_location="Bryant Park",
            class_name="Yoga Sculpt",
            class_duration=45,  # Duration in minutes
            class_date=class_date,
            class_time=datetime.combine(class_date, class_time),  # Combine date and time
            created_at=datetime.utcnow()
        )



        
        db.session.add(workoutclass)
        db.session.commit()


        print("Seeding complete.")