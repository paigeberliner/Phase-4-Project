#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, ClaimedClass, AvailableClass

with app.app_context():

    users = [] 
    claimed_classes = []
    available_classes = []

    users.append(User(email = "test@example.com", first))

