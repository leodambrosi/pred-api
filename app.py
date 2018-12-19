from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
import pickle

"""
curl http://localhost:5000/predict -H application/json --data-binary '{ \
  "crime_rate": 0.1, \
  "avg_number_of_rooms": 4.0, \
  "distance_to_employment_centers": 6.5,\
  "property_tax_rate": 330.0, \
  "pupil_teacher_ratio": 19.5
}'
"""

app = Flask(__name__)
api = Api(app)

model_filename = 'model/house_prediction.pkl'
with open(model_filename, 'rb') as f:
    model = pickle.load(f)

model_filename = 'model/stddev.pkl'
with open(model_filename, 'rb') as f:
    stddev = pickle.load(f)

class PredictHouse(Resource):
    def post(self):
        data = request.get_json(force=True)

        expectedArguments = ['crime_rate', 'avg_number_of_rooms', 'distance_to_employment_centers', 'property_tax_rate', 'pupil_teacher_ratio']
        keys = list(data.keys())

        if set(expectedArguments) == set(keys):

            crime_rate = data['crime_rate']
            avg_number_of_rooms = data['avg_number_of_rooms']
            distance_to_employment_centers = data['distance_to_employment_centers']
            property_tax_rate = data['property_tax_rate']
            pupil_teacher_ratio = data['pupil_teacher_ratio']

            pred = model.predict([[crime_rate, avg_number_of_rooms, distance_to_employment_centers, property_tax_rate,
                                   pupil_teacher_ratio]])

            return jsonify(house_value=round(pred.tolist()[0][0], 1), stddev=round(stddev, 1))

        else:
            return abort(400)

api.add_resource(PredictHouse, '/predict')

if __name__ == '__main__':
    app.run(debug=True)