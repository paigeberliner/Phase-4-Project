from config import db

class User(db.Model): 
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String) 
    first_name = db.Column(db.String) 
    last_name = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    

class AvailableClass(db.Model):
    __tablename__ = 'available_classes'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String) 
    studio = db.Column(db.String)
    class_time = db.Column(db.DateTime)
    class_duration = db.Column(db.Integer)
    address = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users', backref='classes')

class ClaimedClass(db.Model):
    __tablename__ = 'claimed_classes'
    id = db.Column(db.Integer, primary_key=True)
    available_class_id = db.Column(db.Integer, db.ForeignKey('available_classes.id'))
    claimed_time = db.Column(db.DateTime) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    available_class = db.relationship('AvailableClasses', backref='claimed_classes')
    user = db.relationship('Users', backref='claimed_classes')
