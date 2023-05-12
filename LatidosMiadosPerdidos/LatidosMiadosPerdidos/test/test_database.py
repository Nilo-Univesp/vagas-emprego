import unittest
import os
from LatidosMiadosPerdidos.pet_database import PetDatabase

class TestPetDatabase(unittest.TestCase):
    def setUp(self):
        self.pet_db = PetDatabase('test_pets.db')
        self.pet_db.connect()
        self.pet_db.create_table()

    def tearDown(self):
        self.pet_db.disconnect()
        os.remove('test_pets.db')

    def test_add_pet(self):
        pet_data = {
            'name': 'Test Pet',
            'breed': 'Test Breed',
            'description': 'Test Description',
            'contact': 'Test Contact'
        }
        self.assertTrue(self.pet_db.add_pet(pet_data))

    def test_delete_pet(self):
        pet_data = {
            'name': 'Test Pet',
            'breed': 'Test Breed',
            'description': 'Test Description',
            'contact': 'Test Contact'
        }
        pet_id = self.pet_db.add_pet(pet_data)
        self.assertTrue(self.pet_db.delete_pet(pet_id))

    def test_add_pet_incomplete_data(self):
        pet_data = {
            'name': 'Test Pet',
            'breed': 'Test Breed'
        }
        self.assertFalse
