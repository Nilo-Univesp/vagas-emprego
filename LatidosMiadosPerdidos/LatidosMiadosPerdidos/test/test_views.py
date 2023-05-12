import unittest
from LatidosMiadosPerdidos import app
from LatidosMiadosPerdidos.pet_database import PetDatabase

class TestViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.pet_db = PetDatabase('test_pets.db')
        self.pet_db.connect()
        self.pet_db.create_table()

    def tearDown(self):
        self.pet_db.delete_pet_table()
        self.pet_db.disconnect()

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    def test_contact_view(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contato', response.data)

    def test_about_view(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Saiba mais', response.data)

    def test_formpet_view(self):
        response = self.client.get('/formpet')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cadastre um Pet', response.data)

    def test_register_pet_view(self):
        pet_data = {
            'pet-name': 'Test Pet',
            'pet-breed': 'Test Breed',
            'pet-description': 'Test Description',
            'contact': 'Test Contact'
        }
        response = self.client.post('/register-pet', data=pet_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"success":true', response.data)
