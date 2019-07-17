import json
import unittest
from ..app import create_app, db


class RouteTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client
        self.user = {
            'id': 1,
            'name': 'Pedro Di Santi',
            'age': 25,
            'sex': 'Male',
            'cnh': 'A'
        }
        self.route = {
            'id': 1,
            'driver_id': 1,
            'origin_latitude': 25.00,
            'origin_longitude': 20.00,
            'destination_latitude': 500.00,
            'destination_longitude': 725.00,
        }
        with self.app.app_context():
            db.create_all()

    def test_routes_creation(self):
        drivers = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                     data=json.dumps(self.user))
        self.assertEqual(drivers.status_code, 201)

        res = self.client().post('/routes/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.route))
        self.assertEqual(res.status_code, 201)

    def test_route_creation_with_no_origin_latitude(self):
        route1 = {
            'driver_id': 1,
            'origin_longitude': 20.00,
            'destination_latitude': 500.00,
            'destination_longitude': 725.00,
        }
        res = self.client().post('/routes/', headers={'Content-Type': 'application/json'}, data=json.dumps(route1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('origin_latitude'))

    def test_route_creation_with_no_origin_longitude(self):
        route1 = {
            'driver_id': 1,
            'origin_latitude': 25.00,
            'destination_latitude': 500.00,
            'destination_longitude': 725.00,
        }
        res = self.client().post('/routes/', headers={'Content-Type': 'application/json'}, data=json.dumps(route1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('origin_longitude'))

    def test_route_creation_with_no_destination_latitude(self):
        route1 = {
            'driver_id': 1,
            'origin_latitude': 25.00,
            'origin_longitude': 20.00,
            'destination_longitude': 725.00,
        }
        res = self.client().post('/routes/', headers={'Content-Type': 'application/json'}, data=json.dumps(route1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('destination_latitude'))

    def test_route_creation_with_no_destination_longitude(self):
        route1 = {
            'driver_id': 1,
            'origin_latitude': 25.00,
            'origin_longitude': 20.00,
            'destination_latitude': 500.00,
        }
        res = self.client().post('/routes/', headers={'Content-Type': 'application/json'}, data=json.dumps(route1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('destination_longitude'))

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
