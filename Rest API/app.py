from flask import Flask
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

# some data for testing, 2 users with balance
users = [{
  "name": "Adam",
  "owes": {
    "Bob": 12.0,
    "Dan": 9},
  "owed_by": {
    "Bob": 6,
    "Dan": 2,},
  "balance": -13},
  {
  "name": "Lucy",
  "owes": {
    "Bob": 12.0},
  "owed_by": {
    "Dan": 2},
  "balance": 10}
  ]

# flask_restful parser to parse the data from the request
parser = reqparse.RequestParser()
parser.add_argument('user')
parser.add_argument('lender')
parser.add_argument('borrower')
parser.add_argument('amount')

def get_user_index(name):
    """
    fuction to get the index in the list of a given user
    input : name of user (str)
    output : index of the user in the list (int)
    """
    i = 0
    while i < len(users):
        if users[i]['name'] == name:
            return i
        i+=1


def get_users():
    """
    Fuction to get the list of user names
    has no output
    output : list of user names
    """
    users_list = []
    for user in users:
        users_list.append(user['name'])
    return users_list

class Users(Resource):

    def get(self):
        # get list of users
        users_list = get_users()
        # return dict with users list
        return {"users":users_list}

class AddUser(Resource):
    
    def post(self):
        # get arguments from the json in post request
        args = parser.parse_args()
        # create new user only if it do not exist yet
        if args['user'] not in get_users():
            users.append({"name": args['user'], "owes": {}, "owed_by": {}, "balance": 0})
            return 201
        else:
            return "user already exists", 201

class Iou(Resource):

    def post(self):
        args = parser.parse_args()

        if args['lender'] not in get_users():
            return "lender do not exist as a user yet, create it first", 201

        elif args['borrower'] not in get_users():
            return "borrower do not exist as a user yet, create it first", 201

        else:
            # get user id from lender and borrower
            lender_id = get_user_index(args['lender'])
            borrower_id = get_user_index(args['borrower'])

            # add the record owed_by for lender
            users[lender_id]['owed_by'][args['borrower']] = args['amount']
            # add the record of owes for borrower
            users[borrower_id]['owes'][args['lender']] = args['amount']

            # update balance for lender and borrower
            users[lender_id]['balance'] += int(args['amount'])
            users[borrower_id]['balance'] -= int(args['amount'])

            return 201



api.add_resource(Users, '/users')
api.add_resource(AddUser, '/add')
api.add_resource(Iou, '/iou')


if __name__ == '__main__':
    app.run(debug=True)