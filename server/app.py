#!/usr/bin/env python3

from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from datetime import datetime
from flask_cors import CORS

# Local imports
from models import db, User, WorkoutClass, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        user_list = [user.to_dict() for user in users]
        return user_list, 200

    def post(self):
        data = request.get_json()
        new_user = User(
            email=data.get("email"),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            created_at=data.get('created_at', datetime.utcnow())
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201

api.add_resource(UserResource, '/users')

class ReviewResource(Resource):
    def get(self):
        reviews = Review.query.all()
        review_list = [review.to_dict() for review in reviews]
        return review_list, 200

    def post(self):
        data = request.get_json()
        try:
            new_review = Review(
                review=data["review"],
                user_id=data.get('user_id'),
                workoutclass_id=data.get('workoutclass_id')
            )
            db.session.add(new_review)
            db.session.commit()
            return new_review.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 400

api.add_resource(ReviewResource, '/reviews')

class WorkoutClassResource(Resource):
    def get(self):
        workout_classes = WorkoutClass.query.all()
        workout_class_list = [w.to_dict() for w in workout_classes]
        return workout_class_list, 200
    
    def post(self):
        data = request.get_json()
        try:
            class_time_str = data.get('class_time')
            class_time = datetime.strptime(class_time_str, "%H:%M") if class_time_str else None

            new_workout_class = WorkoutClass(
                studio_name=data["studio_name"],
                class_name=data["class_name"],
                studio_location=data["studio_location"],
                class_duration=data["class_duration"],
                class_date=data["class_date"],
                class_time=class_time
            )
            db.session.add(new_workout_class)
            db.session.commit()

            response_body = new_workout_class.to_dict()
            return response_body, 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def delete(self, id):
        workout_class = WorkoutClass.query.get(id)
        if workout_class:
            # Delete associated reviews first
            reviews = Review.query.filter_by(workoutclass_id=id).all()
            for review in reviews:
                db.session.delete(review)
        
            # Then delete the workout class
            db.session.delete(workout_class)
            db.session.commit()
            return {"message": "Record successfully deleted"}, 200
        else:
            return {"error": "Class not found"}, 404
    
    def patch(self, id):
        data = request.get_json()
        email = data.get('email')

        if not email:
            return make_response(jsonify({"error": "Email is required to claim the class"}), 400)

        workout_class = WorkoutClass.query.get(id)
        if not workout_class:
            return make_response(jsonify({"error": "Class not found"}), 404)

        user = User.query.filter_by(email=email).first()
        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        if workout_class.user_claimed:
            return make_response(jsonify({"error": "Class already claimed"}), 400)

        workout_class.user_claimed = user
        db.session.commit()

        response_body = workout_class.to_dict()
        response_body["claimed_by"] = workout_class.user_claimed.email if workout_class.user_claimed else None
        return response_body, 200

api.add_resource(WorkoutClassResource, '/workoutclasses', '/workoutclasses/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
