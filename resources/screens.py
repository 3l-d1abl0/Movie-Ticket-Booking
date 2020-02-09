from flask_restful import Resource, reqparse
from flask import request
from flask import jsonify
from logger import logger
from models.screens import ScreensModel

# api to accept details of a movie screen
class Screens(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="Screen Name")
        parser.add_argument('seatInfo',type=str, required=True, help="Seeting Info !")
        data = parser.parse_args()
        print('data', data)

        model = ScreensModel()
        screen_data = model.find('name',data["name"])
        print('screen_data ',screen_data)
        if screen_data is None:
            try:
                seatMatrix = {}
                data_seat_info = eval(data['seatInfo'])
                print(type(data_seat_info))
                for i in data_seat_info:
                    seat_rows = {}
                    for j in range(data_seat_info[i]['numberOfSeats']):
                        seat_rows[str(j)] = 0

                    seatMatrix[i] = seat_rows

                data['seatMatrix'] = seatMatrix
                print(data)
                model.insert(data)
                return {'message': 'success'}, 200
            except Exception as e:
                logger.error(str(e))
                print(str(e))
                return {'error':'Internal Error'}, 500
        else:
            return { 'message': '{} already exist'.format(data["name"])}, 200

        return {'message': 'success'}, 200

#api to reserve tickets for given seats in a given screen
class ScreensReserve(Resource):

    def post(self, screen_name):

        parser = reqparse.RequestParser()
        parser.add_argument('seats', type=str, required=True, help="Need seats to Book !")
        data = parser.parse_args()

        print(screen_name)
        if screen_name is None or screen_name=='':
            return {'error':'Need Screen Name'}, 400
        print(data)


        model = ScreensModel()
        screen_data = model.find('name',screen_name)
        
        if screen_data is None:
            return {'error':'Screen does not exist'}, 200
        else:

            print('screen_matrix ', screen_data['seatMatrix'])
            try:
                data_seats = eval(data['seats'])
                for seat_row in data_seats:

                    print('seat_row ',seat_row)
                    print(screen_data['seatMatrix'])

                    if seat_row not in screen_data['seatMatrix']:
                        return {'error':'Seats Unavaiilable !'}, 400
                    else:
                        #row exists, loop through it and check
                        for seat in data_seats[seat_row]:
                            if screen_data['seatMatrix'][seat_row][str(seat)]==0:
                                screen_data['seatMatrix'][seat_row][str(seat)]=1
                            else:
                                return {'error':'Seats Unavaiilable '}, 400

                model.save(screen_data)
                print('new_screen_data ', screen_data)
                return {'message':'Reserved'}, 200

            except Exception as e:
                logger.error(str(e))
                print(str(e))
                return {'error':'Internal Error'}, 500

        
        return {'message':'Reserved'}, 200

#api to get the available seats for a given screen
class ScreensAvailable(Resource):

    def get(self, screen_name):
        print('parser')
        parser = reqparse.RequestParser()
        parser.add_argument('status', type=str, required=True, location='args', help="Need to have Status !")
        data = parser.parse_args()
        print('data ', screen_name)

        if screen_name is None or screen_name=='':
            return {'error':'Need Screen Name'}, 400

        if data['status'] is None or data['status']!='unreserved':
            return {'error':'Unknown status'}, 400


        model = ScreensModel()
        screen_data = model.find('name',screen_name)

        if screen_data is None:
            return {'error':'Unknown screen'}, 400

        print(screen_data)
        print('screen_matrix ', screen_data['seatMatrix'])

        seat_dict ={}
        for seat_row in screen_data['seatMatrix']:

            seat_list =[]
            for seat in screen_data['seatMatrix'][seat_row]:
                if screen_data['seatMatrix'][seat_row][str(seat)]==0:
                    seat_list.append(seat)

            seat_dict[seat_row]= seat_list
        
        unreserved ={}
        unreserved["seats"]=seat_dict

        return jsonify(unreserved)