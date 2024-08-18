from config import db
from datetime import datetime
from sqlalchemy.orm import validates


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
    class_date = db.Column(db.String)
    class_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    user_claimed_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @validates('studio_name')
    def validate_studio_name(self, key, studio_name):
        if not studio_name or not isinstance(studio_name, str):
            raise ValueError("Studio name must be a non-empty string")
        return studio_name
    @validates('studio_location')
    def validate_studio_name(self, key, studio_location):
        if not studio_location or not isinstance(studio_location, str):
            raise ValueError("Studio location must be a non-empty string")
        return studio_location
    @validates('class_name')
    def validate_class_name(self, key, class_name):
        if not class_name or not isinstance(class_name, str):
            raise ValueError("Class name must be a non-empty string")
        return class_name
    @validates('class_duration')
    def validate_class_duration(self, key, class_duration):
        if not class_duration or not isinstance(class_duration, int):
            raise ValueError("Class duration must be a non-empty integer")
        return class_duration
    
    
    
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
            'class_time': self.class_time.strftime("%H:%M") if self.class_time else None,
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