from flask import Flask, request
from flask_restful import Resource, Api
from models import Drivers, Cars

app = Flask(__name__)
api = Api(app)

class Driver(Resource):
    def post(self):
        data = request.json
        driver = Drivers(name=data['name'], identity=data['identity'])
        driver.save
        response = {
            'id': driver.id,
            'name': driver.name,
            'identity': driver.identity
        }

        return response

    def get(self, identity):
        driver = Drivers.query.filter_by(identity=identity).first()
        try: 
            response = {
                'id' :driver.id,
                'name':driver.name,
                'identity': driver.identity
            }
        except AttributeError:
            response = {
                'status' :'error',
                'menssage': 'Driver not found'
            }
        return response

    def delete(self, name):
        try:
            driver = Drivers.query.filter_by(name=name).first()
            driver.delete()
            response = {
                'status' :'ok',
                'menssage': 'Driver deleted'
            }

        except AttributeError:
            response = {
                'status' :'error',
                'menssage': 'Driver not found'
            }
        return response
    
class Car(Resource):
    def get(self, plate):
        car = Cars.query.filter_by(plate=plate).first()
        try: 
            response = {
                'id': car.id,
                'driver' :car.driver_id,
                'modek':car.model,
                'plate': car.plate
            }
        except AttributeError:
            response = {
                'status' :'error',
                'menssage': 'Driver not found'
            }
        return response


    def post (self):
        data = request.json
        driver = Drivers.query.filter_by(driver=data[driver]).first()
        car = Cars(model=data['model'], plate=data['plate'], driver_id=driver['identity'])
        car.save
        response = {
            'driver': car.driver_id.identity,
            'plate': car.plate
        }
        print(car)
        return response
    
api.add_resource(Car, '/car/<string:plate>')        
api.add_resource(Driver, '/driver/<string:name>/')

if __name__ == '__main__':
    app.run(debug=True)