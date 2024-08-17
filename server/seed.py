#!/usr/bin/env python3

# Standard library imports
from datetime import datetime

# Local imports
from app import app
from models import db, User, WorkoutClass, Review

if __name__ == '__main__':
    with app.app_context():
        # Drop all tables
        db.drop_all()
        # Create all tables
        db.create_all()

        # Create example user
        user = User(email="paigeberliner@gmail.com", first_name="Paige", last_name="Berliner", created_at=datetime.now())
        db.session.add(user)
        db.session.commit()

        # Create an example of a reivew 
        review = Review (review="I liked this class", user_id= 1, workout_class_id = 1)
        db.session.add(review)
        db.session.commit()
    
        # Create an example workout class
        class_date = datetime.strptime('2024-08-10', '%Y-%m-%d')
        class_time = datetime.strptime('19:00:00', '%H:%M:%S').time()

        workoutclass = WorkoutClass(
            studio_name="CorePower",
            studio_location="Bryant Park",
            class_name="Yoga Sculpt",
            class_duration=45,
            class_date=class_date,
            class_time=datetime.combine(class_date, class_time),
            created_at=datetime.utcnow()
        )
        db.session.add(workoutclass)
        db.session.commit()

        print("Seeding complete.")