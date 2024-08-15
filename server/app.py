#!/usr/bin/env python3

# Remote library imports
from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from datetime import datetime

# Local imports
from config import app, db, api
from models import User, WorkoutClass, Review

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

from flask import Flask, request, jsonify, make_response
from models import db, User
from datetime import datetime

@app.route('/users', methods=['GET', 'POST'])
def users(): 
    if request.method == 'GET':
        users = []
        for user in User.query.all(): 
            user_dict = { 
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name, 
                "created_at": user.created_at
            }
            users.append(user_dict)

        response = make_response(
            jsonify(users),
            200
        )
        return response

    elif request.method == 'POST':
        try:
            data = request.get_json()
            new_user = User(
                email=data["email"],
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                created_at=data.get('created_at', datetime.utcnow())  # Set created_at to now if not provided
            )
            db.session.add(new_user)
            db.session.commit()

            response_body = {
                "message": "User created successfully",
                "user": {
                    "email": new_user.email,
                    "first_name": new_user.first_name,
                    "last_name": new_user.last_name,
                    "created_at": new_user.created_at
                }
            }

            response = make_response(
                jsonify(response_body),
                201
            )
            return response

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 400)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_dict = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "created_at": user.created_at.isoformat() if user.created_at else None
        }
        return make_response(jsonify(user_dict), 200)
    else:
        return make_response(jsonify({"error": "User not found"}), 404)
    
@app.route('/reviews', methods=['GET', 'POST'])
def reviews(): 
    if request.method == 'GET':
        reviews = []
        for review in Review.query.all(): 
            review_dict = { 
                "user": review.user.first_name,
                "workout_class": review.workout_class.class_name,
                "review": review.review
            }
            reviews.append(review_dict)

        response = make_response(
            jsonify(reviews),
            200
        )
        return response

    elif request.method == 'POST':
        try:
            data = request.get_json()
            new_review = Review(
                review=data.get('review'),
                user_id=data.get('user_id')
            )
            db.session.add(new_review)
            db.session.commit()

            response_body = {
                "id": new_review.id,
                "review": new_review.review,
                "user_id": new_review.user_id
            }

            response = make_response(
                jsonify(response_body),
                201
            )
            return response

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 400)


@app.route('/workoutclasses', methods=['GET', 'POST', 'DELETE'])
def workout_classes():
    if request.method == 'GET': 
        workout_classes = []
        for workout_class in WorkoutClass.query.all():
            workout_class_dict = {
                "id": workout_class.id,
                "studio_name": workout_class.studio_name,
                "studio_location": workout_class.studio_location,
                "class_name": workout_class.class_name,
                "class_duration": workout_class.class_duration,
                "class_date": workout_class.class_date.isoformat() if workout_class.class_date else None,
                "class_time": workout_class.class_time.strftime("%H:%M") if workout_class.class_time else None,
                "created_at": workout_class.created_at.isoformat() if workout_class.created_at else None
            }
            workout_classes.append(workout_class_dict)

        response = make_response(
            jsonify(workout_classes),
            200
        )
        return response

    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            return make_response(jsonify({"error": "No input data provided"}), 400)

        try:
            class_date_str = data.get('class_date')
            class_date = datetime.strptime(class_date_str, '%m.%d.%Y') if class_date_str else None
            class_time_str = data.get('class_time')
            class_time = datetime.strptime(class_time_str, "%H:%M").time() if class_time_str else None

            new_workout_class = WorkoutClass(
                studio_name=data.get('studio_name'),
                studio_location=data.get('studio_location'),
                class_name=data.get('class_name'),
                class_duration=data.get('class_duration'),
                class_date=class_date,
                class_time=class_time,
                created_at=datetime.utcnow()
            )
            db.session.add(new_workout_class)
            db.session.commit()

            response_body = {
                "id": new_workout_class.id,
                "studio_name": new_workout_class.studio_name,
                "studio_location": new_workout_class.studio_location,
                "class_name": new_workout_class.class_name,
                "class_duration": new_workout_class.class_duration,
                "class_date": new_workout_class.class_date.isoformat() if new_workout_class.class_date else None,
                "class_time": new_workout_class.class_time.strftime("%H:%M") if new_workout_class.class_time else None,
                "created_at": new_workout_class.created_at.isoformat() if new_workout_class.created_at else None
            }

            response = make_response(
                jsonify(response_body),
                201
            )
            return response
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 400)
    
    elif request.method == 'DELETE':
        data = request.get_json()
        workout_class_id = data.get('id')
        if not workout_class_id:
            return make_response(jsonify({"error": "No class ID provided"}), 400)

        workout_class = WorkoutClass.query.get(workout_class_id)
        if not workout_class:
            return make_response(jsonify({"error": "Class not found"}), 404)

        db.session.delete(workout_class)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Class deleted."
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)