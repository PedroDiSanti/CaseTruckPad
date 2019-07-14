from flask import Flask

from .models import db
from .config import app_config

from .views.RouteView import route_api as route_blueprint
from .views.DriverView import driver_api as driver_blueprint
from .views.VehicleView import vehicle_api as vehicle_blueprint


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    db.init_app(app)

    # Endpoint for routes
    app.register_blueprint(route_blueprint, url_prefix='/routes')

    # Endpoint for drivers
    app.register_blueprint(driver_blueprint, url_prefix='/drivers')

    # Endpoint for vehicles
    app.register_blueprint(vehicle_blueprint, url_prefix='/vehicles')

    @app.route('/', methods=['GET'])
    def index():
        return 'Great! This is working.'

    return app
