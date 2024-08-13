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

@app.route('/users', methods=['GET'])
def users(): 
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

@app.route('/reviews', methods=['GET'])
def reviews(): 
    reviews = []
    for review in Review.query.all(): 
        review_dict = { 
            "user": review.user.first_name,
            "review": review.review
        }
        reviews.append(review_dict)

    response = make_response(
        jsonify(reviews),
        200
    )

    return response

@app.route('/workoutclasses', methods=['GET', 'POST'])
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
                "class_time": workout_class.class_time.strftime("%H:%M") if workout_class.class_time else None,  # Format time
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
            class_date = datetime.strptime(class_date_str('class_date'), '%m.%d.%Y') if data.get('class_date') else None
            class_time_str = data.get('class_time')
            class_time = datetime.strptime(class_time_str, "%H:%M").time() if class_time_str else None

            new_workout_class = WorkoutClass(
                studio_name=data.get('studio_name'),
                studio_location=data.get('studio_location'),
                class_name=data.get('class_name'),
                class_duration=data.get('class_duration'),
                class_date=class_date,
                class_time=class_time,
                created_at=datetime.utcnow()  # Set to current time
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
                "class_time": new_workout_class.class_time.strftime("%H:%M") if new_workout_class.class_time else None,  # Format time
                "created_at": new_workout_class.created_at.isoformat() if new_workout_class.created_at else None
            }

            response = make_response(
                jsonify(response_body),
                201
            )
            return response

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)