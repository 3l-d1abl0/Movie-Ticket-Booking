'''from flask_mongoengine import MongoEngine

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
'''
import mongoengine

#collection Name
'''
mongo = ''

from flask_pymongo import PyMongo'''

def initialize_db(app):
    global mongo
    mongo = PyMongo(app)
    print('init_db')
    print(mongo)
    print('+init+')
    screens = mongo.db.tickets
#screens.find_one({'name':screen_name})