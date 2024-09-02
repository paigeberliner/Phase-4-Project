from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import validates

db = SQLAlchemy()

class User(db.Model): 
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    reviews = db.relationship('Review', back_populates='user')
    workoutclasses_claimed = db.relationship('WorkoutClass', back_populates='user_claimed')

    # Serialize rules
    serialize_rules = ('-reviews.user', '-workoutclasses_claimed.user_claimed')

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat()
        }

class WorkoutClass(db.Model): 
    __tablename__ = 'workoutclasses'
    
    id = db.Column(db.Integer, primary_key=True)
    studio_name = db.Column(db.String, nullable=False)
    studio_location = db.Column(db.String, nullable=False)
    class_name = db.Column(db.String, nullable=False)
    class_duration = db.Column(db.Integer, nullable=False)
    class_date = db.Column(db.String)
    class_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    user_claimed_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationships
    user_claimed = db.relationship('User', back_populates='workoutclasses_claimed')
    reviews = db.relationship('Review', back_populates='workoutclass')

    # Serialize rules
    serialize_rules = ('-user_claimed.workoutclasses_claimed', '-reviews.workoutclass')

    def to_dict(self):
        return {
            'id': self.id,
            'studio_name': self.studio_name,
            'studio_location': self.studio_location,
            'class_name': self.class_name,
            'class_duration': self.class_duration,
            'class_date': self.class_date,
            'class_time': self.class_time.strftime("%H:%M") if self.class_time else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'user_claimed_id': self.user_claimed_id
        }

    @validates('studio_name')
    def validate_studio_name(self, key, studio_name):
        if not studio_name or not isinstance(studio_name, str):
            raise ValueError("Studio name must be a non-empty string")
        return studio_name

    @validates('studio_location')
    def validate_studio_location(self, key, studio_location):
        if not studio_location or not isinstance(studio_location, str):
            raise ValueError("Studio location must be a non-empty string")
        return studio_location

    @validates('class_name')
    def validate_class_name(self, key, class_name):
        if not class_name or not isinstance(class_name, str):
            raise ValueError("Class name must be a non-empty string")
        return class_name

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String, nullable=False)
    #rating = db.Column(db.Integer, nullable=False)
    #created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='reviews')

    workoutclass_id = db.Column(db.Integer, db.ForeignKey('workoutclasses.id'), nullable=False)
    workoutclass = db.relationship('WorkoutClass', back_populates='reviews')

    # Serialize rules
    serialize_rules = ('-user.reviews', '-workoutclass.reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'review': self.review,
            #'rating': self.rating,
            #'created_at': self.created_at.isoformat(),
            'user_id': self.user_id,
            'workoutclass_id': self.workoutclass_id, 
            'user': self.user.first_name if self.user else None,
        }
