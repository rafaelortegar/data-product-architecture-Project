from flask import Flask
from flask_restx import Api, Resource, fields
from src.deploy.market import get_prediction

app = Flask(__name__)
api = Api(app, version='1.0', title='Afluencia Metro API',
    description='API de modelo de Afluencia metro',
)

ns = api.namespace('predicts', description='FLIGHTS operations')

predict = api.model('Delay', {
    'flight_number': fields.Integer(readOnly=True, description='The flight unique identifier')
})

#1609
@ns.route('/<int:flight_number>')
@ns.response(404, 'Delay not found')
@ns.response(404, 'Flight number not found')
@ns.response(200, 'Delay prediction')
@ns.param('flight_number', 'The flight identifier')

class Delay(Resource):
    '''Show a single predict item and lets you delete them'''
    @ns.doc('get_predict')
    def get(self, flight_number):
        '''Fetch a given resource'''
        result = get_prediction(flight_number)
        return str(result)

if __name__ == '__main__':
    app.run(debug=True)