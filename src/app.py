from flask import Flask
from flask_restful import Api
import controllers.usuario_controller as UsuarioController

app = Flask(__name__)
api = Api(app)

api.add_resource(UsuarioController.getSigleUser, '/user/<int:_id>')
api.add_resource(UsuarioController.getListUsers, '/users')
api.add_resource(UsuarioController.createNewUser, '/user')
api.add_resource(UsuarioController.deleteUser, '/user')
api.add_resource(UsuarioController.Update, '/user')

if __name__ == "__main__":
    app.run(debug=True, port=8002)
