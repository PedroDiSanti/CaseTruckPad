from flask import request, Blueprint, json, Response
from ..models.VehicleModel import VehicleModel, VehicleSchema

vehicle_api = Blueprint('vehicle_api', __name__)
vehicle_schema = VehicleSchema()


@vehicle_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    data, error = vehicle_schema.load(req_data)
    if error:
        return custom_response(error, 400)

    post = VehicleModel(data)
    post.save()

    data = vehicle_schema.dump(post).data
    return custom_response(data, 201)


@vehicle_api.route('/truck_today', methods=['GET'])
def list_trucks_today():
    vehicle = VehicleModel.get_trucks_today()

    response = vehicle_schema.dump(vehicle, many=True).data
    return custom_response(response, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
