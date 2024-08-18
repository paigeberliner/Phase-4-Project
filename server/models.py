from config import db
from datetime import datetime


class User(db.Model): 
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)  # Added constraints
    first_name = db.Column(db.String(50), nullable=False)  # Added constraints
    last_name = db.Column(db.String(50), nullable=False)  # Added constraints
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relationship mapping the user to related reviews
    reviews = db.relationship('Review', back_populates="user")
    
    # Relationship mapping the user to claimed workout classes
    workoutclasses_claimed = db.relationship('WorkoutClass', back_populates="user_claimed")

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat()  # Convert datetime to string
        }


class WorkoutClass(db.Model): 
    __tablename__ = 'workoutclasses'
    
    id = db.Column(db.Integer, primary_key=True) 
    studio_name = db.Column(db.String)
    studio_location = db.Column(db.String)
    class_name = db.Column(db.String) 
    class_duration = db.Column(db.Integer)
    class_date = db.Column(db.DateTime)
    class_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    user_claimed_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    
    # Relationship mapping the workout class to related reviews
    reviews = db.relationship('Review', back_populates="workout_class")
    
    # Relationship mapping the workout class to the user who claimed it
    user_claimed = db.relationship('User', back_populates="workoutclasses_claimed")

    def to_dict(self):
        return {
            'id': self.id,
            'studio_name': self.studio_name, 
            'studio_location': self.studio_location, 
            'class_name': self.class_name,
            'class_duration': self.class_duration,
            'class_date': self.class_date,
            'class_time': self.class_time,
            'created_at': self.created_at,
            'user_claimed': self.user_claimed_id
        }


class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    workout_class_id = db.Column(db.Integer, db.ForeignKey('workoutclasses.id'))
    
    # Relationship mapping the review to related user and workout class
    user = db.relationship('User', back_populates="reviews")
    workout_class = db.relationship('WorkoutClass', back_populates="reviews")

    def to_dict(self):
        return {
            'id': self.id,
            'review': self.review,
            'user': self.user.first_name if self.user else None,
            'workout_class': self.workout_class.class_name if self.workout_class else None
        }