from mongoengine import connect


temp = connect("screen", port=27017, host='localhost')

db = temp['screen']