from .db import db

class ScreensModel():
    #screens = mongo.db.tickets

    def __init__(self):
        '''
        mongo.reload(mongo)
        print(mongo)
        self.screens = mongo.db.screens'''
        self.collection = db.get_collection("ticket")
        #print(dir(self.collection))

    def find(self, key, screen_name):
        screen_data = self.collection.find_one({key:screen_name})
        return screen_data

    def insert(self, data):
        status = self.collection.insert(data)
        print(status)

    def save(self, data):
        status = self.collection.save(data)
        print(status)