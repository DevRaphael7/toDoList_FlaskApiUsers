from flask import request
from flask_restful import Resource, reqparse
from db.users_db import users
from models.usuario import Usuario

class getSigleUser(Resource):

    def get(self, _id: int):
        user = [user.__dict__ for user in users if user.id == _id]
        return { "usuario": user }, 200 if not user else 404
    
class getListUsers(Resource):

    def get(self):
        return { "usuarios": [user.__dict__ for user in users] }
    
class createNewUser(Resource):

    def post(self):
        request_body = request.get_json()

        if [user for user in users if user.name == request_body["name"]]:
            return { "message": "This user is alredy exist."}, 400

        new_user = Usuario(request_body["name"], request_body["age"], (users[-1].id + 1) if users else 1)
        users.append(new_user)
        return { "message": f"User {request_body['name']} created with success!" }, 201
    
class deleteUser(Resource):

    def delete(self):
        global users

        request_body = request.get_json()
        
        checkFound = [user for user in users if user.id == request_body["id"]]

        if checkFound:
            users = [user for user in users if user.id != request_body["id"]]
            return { "message": "user deleted with success!" }
        else:
            return { "message": "User not found" }, 404
        
class Update(Resource):

    def put(self):
        parse = reqparse.RequestParser()

        parse.add_argument('id', 
            type=int,
            required=True,
            help="Field id is required"
        )

        parse.add_argument('name', 
            type=str,
            required=True,
            help="Field name is required"
        )

        parse.add_argument('age', 
            type=int,
            required=False,
        )

        global users
        request_body = parse.parse_args()
        userIndex = [index for index in range(len(users)) if users[index].id == request_body["id"]]

        if not userIndex:
            return { "message": "User not found!" }, 400
            
        users.insert(userIndex[0], Usuario(age= (request_body["age"] if request_body["age"] else users[userIndex[0]].age), name=request_body["name"], _id=request_body["id"]))
        users.pop(userIndex[0] + 1)
        return { "message": "User update with sucess!" }, 200