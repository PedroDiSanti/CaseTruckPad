import json
import unittest
from ..app import create_app, db


class UsersTest(unittest.TestCase):
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

    def test_user_creation(self):
        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

    def test_user_creation_with_existing_name(self):
        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 400)

    def test_user_creation_with_no_name(self):
        user1 = {
            'age': 25,
            'sex': 'Male',
            'cnh': 'A'
        }

        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('name'))

    def test_user_creation_with_no_age(self):
        user1 = {
            'name': 'Pedro Di Santi',
            'sex': 'Male',
            'cnh': 'A'
        }

        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('age'))

    def test_user_creation_with_no_sex(self):
        user1 = {
            'name': 'Pedro Di Santi',
            'age': 25,
            'cnh': 'A'
        }

        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('sex'))

    def test_user_creation_with_no_cnh(self):
        user1 = {
            'name': 'Pedro Di Santi',
            'age': 25,
            'sex': 'Male',
        }

        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('cnh'))

    def test_user_get(self):
        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().get('/drivers/1', headers={'Content-Type': 'application/json'})
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

        self.assertEqual(json_data.get('id'), 1)
        self.assertEqual(json_data.get('name'), 'Pedro Di Santi')
        self.assertEqual(json_data.get('age'), 25)
        self.assertEqual(json_data.get('sex'), 'Male')
        self.assertEqual(json_data.get('cnh'), 'A')

    def test_user_update_name(self):
        user1 = {
            'name': 'new name'
        }

        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().put('/drivers/1', headers={'Content-Type': 'application/json'},
                                data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

        self.assertEqual(json_data.get('name'), 'new name')

    def test_user_update_age(self):
        user1 = {
            'age': 29
        }

        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().put('/drivers/1', headers={'Content-Type': 'application/json'},
                                data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data.get('age'), 29)

    def test_user_update_sex(self):
        user1 = {
            'sex': 'Female'
        }

        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().put('/drivers/1', headers={'Content-Type': 'application/json'},
                                data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data.get('sex'), 'Female')

    def test_user_update_cnh(self):
        user1 = {
            'cnh': 'B'
        }

        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().put('/drivers/1', headers={'Content-Type': 'application/json'},
                                data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data.get('cnh'), 'B')

    def test_delete_user(self):
        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().delete('/drivers/1', headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def test_user_get_list_not_owned(self):
        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.vehicle))
        self.assertEqual(res.status_code, 201)

        res = self.client().get('/drivers/list_not_loaded', headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def test_user_get_list_trucks_owned(self):
        res = self.client().post('/drivers/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

        res = self.client().post('/vehicles/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.vehicle))
        self.assertEqual(res.status_code, 201)

        res = self.client().get('/drivers/list_trucks_owned', headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
