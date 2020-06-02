from flask import Flask
from flask_restplus import Api, Resource
from werkzeug.utils import cached_property
app = Flask(__name__)
api = Api(app)

@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'DPA world!'}

if __name__ == '__main__':
    app.run()