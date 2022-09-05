from flask import Flask
from flask_restful import Api
import controllers.usuario_controller as UsuarioController

app = Flask(__name__)
api = Api(app)

api.add_resource(UsuarioController.getSigleUser, '/user/<int:_id>')
api.add_resource(UsuarioController.getListUsers, '/users')
api.add_resource(UsuarioController.createNewUser, '/user')

app.run(debug=True)
