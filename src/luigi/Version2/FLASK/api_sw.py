from flask import Flask
from flask_restplus import Api, Resource
app = Flask(__name__)
api = Api(app)

@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'DPA world!'}

if __name__ == '__main__':
    app.run()