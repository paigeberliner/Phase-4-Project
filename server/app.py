#!/usr/bin/env python3

# Remote library imports
from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource

# Local imports
from config import app, db, api
from models import User

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

if __name__ == '__main__':
    app.run(port=5555, debug=True)
