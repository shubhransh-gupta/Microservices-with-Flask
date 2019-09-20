from flask import Flask
from flask_restful import Resource, Api, reqparse
from collections import OrderedDict

app = Flask(__name__)
api = Api(app)

user_accounts = OrderedDict()

class AccountsListResource(Resource):
    def get(self):
        return user_accounts
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        args = parser.parse_args()
        args['id'] = len(user_accounts) + 1 
        user_accounts[args['id']] = args
        return args, 201

class AccountsResource(Resource):
    def get(self, id):
        try:
            return user_accounts[id]
        except KeyError as e:
            return {'error_code': 'invalid_account_no', 'message': 'Invalid user account requested'}, 400
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=False)
        parser.add_argument('email', type=str, required=False)
        args = parser.parse_args()
        args['id'] = id
        user_accounts[id] = args
        return args, 200

    def delete(self, id):
        try:
            del user_accounts[id]
            return ''
        except KeyError as e:
            return {'error_code': 'invalid_account_no', 'message': 'Invalid user account requested'}, 400

api.add_resource(AccountsListResource, '/accounts')
api.add_resource(AccountsResource, '/accounts/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)


