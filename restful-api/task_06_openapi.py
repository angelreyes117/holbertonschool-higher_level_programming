#!/usr/bin/env python3
from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title='Sample API', description='A simple API with OpenAPI docs')

ns = api.namespace('users', description='User operations')

user_model = api.model('User', {
    'username': fields.String(required=True),
    'name': fields.String,
    'age': fields.Integer,
    'city': fields.String
})

users = {}

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    def get(self):
        return list(users.keys())

@ns.route('/<username>')
class User(Resource):
    @ns.doc('get_user')
    def get(self, username):
        return users.get(username, {"error": "User not found"})

@ns.route('/add')
class UserAdd(Resource):
    @ns.doc('add_user')
    @ns.expect(user_model)
    def post(self):
        data = api.payload
        if 'username' not in data:
            return {"error": "Username is required"}, 400
        username = data['username']
        users[username] = data
        return {"message": "User added", "user": data}, 201

if __name__ == '__main__':
    app.run(port=5000)
