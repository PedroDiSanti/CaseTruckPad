from flask import request, g, Blueprint, json, Response
from ..models.RouteModel import RouteModel, RouteSchema

route_api = Blueprint('route_api', __name__)
route_schema = RouteSchema()


@route_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    data, error = route_schema.load(req_data)
    if error:
        return custom_response(error, 400)

    post = RouteModel(data)
    post.save()

    data = route_schema.dump(post).data
    return custom_response(data, 201)


@route_api.route('/list_origin', methods=['GET'])
def list_origin():
    origin = RouteModel.list_origin()

    response = route_schema.dump(origin, many=True).data
    return custom_response(response, 200)


@route_api.route('/list_destination', methods=['GET'])
def list_destination():
    destination = RouteModel.list_destination()

    response = route_schema.dump(destination, many=True).data
    return custom_response(response, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
