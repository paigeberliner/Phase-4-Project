from config import db

class User(db.Model): 
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String) 
    first_name = db.Column(db.String) 
    last_name = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    
    # Relationship mapping the user to related reviews
    reviews = db.relationship('Review', back_populates="user")


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
    
    # Relationship mapping the workout class to related reviews
    reviews = db.relationship('Review', back_populates="workout_class")


class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    workout_class_id = db.Column(db.Integer, db.ForeignKey('workoutclasses.id'))
    
    # Relationship mapping the review to related user and workout class
    user = db.relationship('User', back_populates="reviews")
    workout_class = db.relationship('WorkoutClass', back_populates="reviews")
