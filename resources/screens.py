from flask_restful import Resource, reqparse
from flask import request
import json
from logger import logger


# api to accept details of a movie screen
class Screens(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="Screen Name")
        parser.add_argument('seatInfo',type=str, required=True, help="Seeting Info !")
        data = parser.parse_args()

        #data = json.loads(request.data)

        logger.info(data)
        print(data)

        return {'message': 'screens'}, 200


class ScreensReserve(Resource):

    def post(self, screen_name):

        parser = reqparse.RequestParser()
        parser.add_argument('seats', type=str, required=True, help="Need seats to Book !")
        data = parser.parse_args()

        logger.info(screen_name)
        logger.info(data)

        return {'message':'Reserved'}, 200


class ScreensAvailable(Resource):

    def get(self, screen_name):
        parser = reqparse.RequestParser()
        parser.add_argument('seats', type=str, required=True, help="Need seats to check Reservations !")
        parser.add_argument('status', type=str, required=True, help="Need to have Status !")
        data = parser.parse_args()

        logger.info(screen_name)
        logger.info(data)

        return {'message':'Reserved'}, 200