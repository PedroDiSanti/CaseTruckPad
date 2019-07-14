from flask import request, json, Response, Blueprint
from ..models.DriverModel import DriverModel, DriverSchema

driver_api = Blueprint('drivers', __name__)
driver_schema = DriverSchema()


@driver_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    data, error = driver_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    driver_in_db = DriverModel.get_driver_by_name(data.get('name'))
    if driver_in_db:
        return custom_response({'Error': 'Driver already exist.'}, 400)

    driver = DriverModel(data)
    driver.save()

    response = driver_schema.dump(driver).data
    return custom_response(response, 201)


@driver_api.route('/<int:driver_id>', methods=['GET'])
def get(driver_id):
    driver = DriverModel.get_one_driver(driver_id)
    if not driver:
        return custom_response({'Error': 'Driver not found.'}, 404)

    response = driver_schema.dump(driver).data
    return custom_response(response, 200)


@driver_api.route('/<int:driver_id>', methods=['PUT'])
def update(driver_id):
    req_data = request.get_json()
    data, error = driver_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)

    driver = DriverModel.get_one_driver(driver_id)
    driver.update(data)

    response = driver_schema.dump(driver).data
    return custom_response(response, 200)


@driver_api.route('/<int:driver_id>', methods=['DELETE'])
def delete(driver_id):
    driver = DriverModel.get_one_driver(driver_id)
    driver.delete()

    return custom_response({'Sucess': 'Driver deleted with sucess!'}, 204)


def custom_response(response, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(response),
        status=status_code
    )
