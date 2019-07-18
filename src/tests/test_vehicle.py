import json
import unittest
from ..app import create_app, db


class VehicleTest(unittest.TestCase):
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
        self.vehicle = {
            'id': 1,
            'driver_id': 1,
            'name': 'Caminhão',
            'type': 2,
            'own_vehicle': True,
            'is_loaded': True
        }
        with self.app.app_context():
            db.create_all()

    def test_vehicles_creation(self):
        drivers = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                     data=json.dumps(self.user))
        self.assertEqual(drivers.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.vehicle))
        self.assertEqual(res.status_code, 201)

    def test_vehicle_creation_with_no_name(self):
        vehicle1 = {
            'driver_id': 1,
            'type': 2,
            'own_vehicle': True,
            'is_loaded': True
        }

        drivers = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                     data=json.dumps(self.user))
        self.assertEqual(drivers.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(vehicle1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)

        self.assertTrue(json_data.get('name'))

    def test_vehicle_creation_with_no_type(self):
        vehicle1 = {
            'driver_id': 1,
            'name': 'Caminhão',
            'own_vehicle': True,
            'is_loaded': True
        }

        drivers = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                     data=json.dumps(self.user))
        self.assertEqual(drivers.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(vehicle1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)

        self.assertTrue(json_data.get('type'))

    def test_vehicle_creation_with_no_own_vehicle(self):
        vehicle1 = {
            'driver_id': 1,
            'name': 'Caminhão',
            'type': 2,
            'is_loaded': True
        }

        drivers = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                     data=json.dumps(self.user))
        self.assertEqual(drivers.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(vehicle1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)

        self.assertTrue(json_data.get('own_vehicle'))

    def test_vehicle_creation_with_no_is_loaded(self):
        vehicle1 = {
            'driver_id': 1,
            'name': 'Caminhão',
            'type': 2,
            'own_vehicle': True,
        }

        drivers = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                     data=json.dumps(self.user))
        self.assertEqual(drivers.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(vehicle1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)

        self.assertTrue(json_data.get('is_loaded'))

    def test_vehicle_get_today(self):
        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.vehicle))
        self.assertEqual(res.status_code, 201)

        res = self.client().get('/vehicles/truck_today', headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def test_vehicle_get_week(self):
        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.vehicle))
        self.assertEqual(res.status_code, 201)

        res = self.client().get('/vehicles/truck_week', headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def test_vehicle_get_month(self):
        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.vehicle))
        self.assertEqual(res.status_code, 201)

        res = self.client().get('/vehicles/truck_month', headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
