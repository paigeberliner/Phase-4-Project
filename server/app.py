#!/usr/bin/env python3

# Remote library imports
from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from datetime import datetime
from flask_cors import CORS

# Local imports
from config import app, db, api
from models import User, WorkoutClass, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app, resources={r"/*": {"origins": "*"}})

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


class UserResource(Resource):
    def get(self):
        response_dict_list = [u.to_dict() for u in User.query.all()] 

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response

    def post(self):
        data = request.get_json()
        new_user = User(
            email=data["email"],
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            created_at=data.get('created_at', datetime.utcnow())  # Set created_at to now if not provided
            )

        db.session.add(new_user)
        db.session.commit()

        response_dict = new_user.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response

api.add_resource(UserResource, '/users')

class UserIDResource(Resource):
    def get(self, user_id):
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

api.add_resource(UserIDResource, '/users/<int:user_id>') 


class ReviewResource(Resource):
    def get(self):
        response_dict_list = [r.to_dict() for r in Review.query.all()] 

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response

    def post(self):
        data = request.get_json()
        new_review = Review(
            review=data["review"],
            user_id=data.get('user_id'), 
            workout_class_id=data.get('workout_class_id')
            )

        db.session.add(new_review)
        db.session.commit()

        response_dict = new_review.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response

api.add_resource(ReviewResource, '/reviews')

class WorkoutClassResource(Resource):
    def get(self):
        response_dict_list = [w.to_dict() for w in WorkoutClass.query.all()] 

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response
    
    def post(self):
        data = request.get_json()
        try:
            class_date_str = data.get('class_date')
            class_date = datetime.strptime(class_date_str, '%Y-%m-%d') if class_date_str else None
            class_time_str = data.get('class_time')
            class_time = datetime.strptime(class_time_str, "%H:%M") if class_time_str else None

            new_workout_class = WorkoutClass(
                studio_name=data["studio_name"],
                class_name=data["class_name"],
                studio_location=data["studio_location"],
                class_duration=data["class_duration"],
                class_date=class_date,
                class_time=class_time
            )

            db.session.add(new_workout_class)
            db.session.commit()

            response_body = {
                 "id": new_workout_class.id,
                 "studio_name": new_workout_class.studio_name,
                 "studio_location": new_workout_class.studio_location,
                 "class_name": new_workout_class.class_name,
                 "class_duration": new_workout_class.class_duration,
                 "class_date": new_workout_class.class_date,#isoformat() if new_workout_class.class_date else None,
                 "class_time": new_workout_class.class_time,#.strftime("%H:%M") if new_workout_class.class_time else None,
                 "created_at": new_workout_class.created_at.isoformat() if new_workout_class.created_at else None
             }
            return jsonify(response_body.to_dict()), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def delete(self, id):
        workoutclass = WorkoutClass.query.filter(WorkoutClass.id == id).first()
        if workoutclass:
            db.session.delete(workoutclass)
            db.session.commit()
            response_dict = {"message": "Record successfully deleted"}
            response = make_response(
                jsonify(response_dict),
                200
            )
        else:
            response_dict = {"error": "Class not found"}
            response = make_response(
                jsonify(response_dict),
                404
            )
        return response
    
    def patch(self, id):
        data = request.get_json()
        email = data.get('email')

        if not email:
            return make_response(jsonify({"error": "Email is required to claim the class"}), 400)

        workout_class = WorkoutClass.query.filter(WorkoutClass.id == id).first()
        if not workout_class:
            return make_response(jsonify({"error": "Class not found"}), 404)

        user = User.query.filter_by(email=email).first()
        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        if workout_class.user_claimed:
            return make_response(jsonify({"error": "Class already claimed"}), 400)

        workout_class.user_claimed = user
        db.session.commit()

        response_body = {
            "id": workout_class.id,
            "studio_name": workout_class.studio_name,
            "studio_location": workout_class.studio_location,
            "class_name": workout_class.class_name,
            "class_duration": workout_class.class_duration,
            "class_date": workout_class.class_date.isoformat() if workout_class.class_date else None,
            "class_time": workout_class.class_time.strftime("%H:%M") if workout_class.class_time else None,
            "created_at": workout_class.created_at.isoformat() if workout_class.created_at else None,
            "claimed_by": workout_class.user_claimed.email if workout_class.user_claimed else None
        }

        response = make_response(
            jsonify(response_body),
            200
        )
        return response 

api.add_resource(WorkoutClassResource, '/workoutclasses', '/workoutclasses/<int:id>')



# @app.route('/workoutclasses', methods=['GET', 'POST', 'DELETE', 'PATCH'])
# def workout_classes():
#     if request.method == 'GET': 
#         workout_classes = []
#         for workout_class in WorkoutClass.query.all():
#             workout_class_dict = {
#                 "id": workout_class.id,
#                 "studio_name": workout_class.studio_name,
#                 "studio_location": workout_class.studio_location,
#                 "class_name": workout_class.class_name,
#                 "class_duration": workout_class.class_duration,
#                 "class_date": workout_class.class_date.isoformat() if workout_class.class_date else None,
#                 "class_time": workout_class.class_time.strftime("%H:%M") if workout_class.class_time else None,
#                 "created_at": workout_class.created_at.isoformat() if workout_class.created_at else None
#             }
#             workout_classes.append(workout_class_dict)

#         response = make_response(
#             jsonify(workout_classes),
#             200
#         )
#         return response

#     elif request.method == 'POST':
#         data = request.get_json()
#         print(data)
#         if not data:
#             return make_response(jsonify({"error": "No input data provided"}), 400)

#         try:
#             class_date_str = data.get('class_date')
#             class_date = datetime.strptime(class_date_str, '%Y-%m-%d') if class_date_str else None
#             class_time_str = data.get('class_time')
#             class_time = datetime.strptime(class_time_str, "%H:%M") if class_time_str else None
#             #breakpoint()
#             new_workout_class = WorkoutClass(
#                 studio_name=data.get('studio_name'),
#                 studio_location=data.get('studio_location'),
#                 class_name=data.get('class_name'),
#                 class_duration=data.get('class_duration'),
#                 class_date=class_date,
#                 class_time=class_time,
#                 created_at=datetime.utcnow()
#             )
#             db.session.add(new_workout_class)
#             db.session.commit()

#             response_body = {
#                 "id": new_workout_class.id,
#                 "studio_name": new_workout_class.studio_name,
#                 "studio_location": new_workout_class.studio_location,
#                 "class_name": new_workout_class.class_name,
#                 "class_duration": new_workout_class.class_duration,
#                 "class_date": new_workout_class.class_date,#isoformat() if new_workout_class.class_date else None,
#                 "class_time": new_workout_class.class_time,#.strftime("%H:%M") if new_workout_class.class_time else None,
#                 "created_at": new_workout_class.created_at.isoformat() if new_workout_class.created_at else None
#             }

#             response = make_response(
#                 jsonify(response_body),
#                 201
#             )
#             return response
#         except Exception as e:
#             return make_response(jsonify({"error": str(e)}), 400)
    
#     elif request.method == 'DELETE':
#         data = request.get_json()
#         workout_class_id = data.get('id')
#         if not workout_class_id:
#             return make_response(jsonify({"error": "No class ID provided"}), 400)

#         workout_class = WorkoutClass.query.get(workout_class_id)
#         if not workout_class:
#             return make_response(jsonify({"error": "Class not found"}), 404)

#         db.session.delete(workout_class)
#         db.session.commit()

#         response_body = {
#             "delete_successful": True,
#             "message": "Class deleted."
#         }

#         response = make_response(
#             jsonify(response_body),
#             200
#         )

#         return response
    
#     elif request.method == 'PATCH':
#         data = request.get_json()
#         workout_class_id = data.get('id')
#         email = data.get('email')
        
#         if not workout_class_id:
#             return make_response(jsonify({"error": "No class ID provided"}), 400)
        
#         workout_class = WorkoutClass.query.get(workout_class_id)
#         if not workout_class:
#             return make_response(jsonify({"error": "Class not found"}), 404)
        
#         if email:
#             user = User.query.filter_by(email=email).first()
#             if not user:
#                 return make_response(jsonify({"error": "User not found"}), 404)

#             if workout_class.user_claimed:
#                 return make_response(jsonify({"error": "Class already claimed"}), 400)

#             workout_class.user_claimed = user
#         else:
#             return make_response(jsonify({"error": "Email is required to claim the class"}), 400)

#         db.session.commit()
        
#         response_body = {
#             "id": workout_class.id,
#             "studio_name": workout_class.studio_name,
#             "studio_location": workout_class.studio_location,
#             "class_name": workout_class.class_name,
#             "class_duration": workout_class.class_duration,
#             "class_date": workout_class.class_date.isoformat() if workout_class.class_date else None,
#             "class_time": workout_class.class_time.strftime("%H:%M") if workout_class.class_time else None,
#             "created_at": workout_class.created_at.isoformat() if workout_class.created_at else None,
#             "claimed_by": workout_class.user_claimed.email if workout_class.user_claimed else None
#         }

#         response = make_response(
#             jsonify(response_body),
#             200
#         )
#         return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)