import os
from flask import Flask
from flask_restful import Api
#from models.db import initialize_db
from resources.screens import Screens, ScreensReserve, ScreensAvailable


app = Flask(__name__)
api = Api(app)
'''
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/screens'
}
'''
#initialize_db(app)


#Routes Configuration
api.add_resource(Screens, '/screens')
api.add_resource(ScreensReserve, '/screens/<screen_name>/reserve')
api.add_resource(ScreensAvailable, '/screens/<screen_name>/seats')

if __name__ == '__main__':
    port = int(os.environ.get('PORT',9090))
    app.run(port=port, debug=True)