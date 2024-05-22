from django.test import TestCase, Client
from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.Marka_car = models.Marka_car.objects.create(
            title='Porshe'
        )
        self.Car = models.Car.objects.create(
            car_name='Priora',
            car_body='хэтчбек',
        )

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_detail_car(self):
        response = self.client.get('/car/')
        self.assertEqual(response.status_code, 200)

    def test_carmark(self):
        response = self.client.get(f'/mark/{self.Car.id}')
        self.assertEqual(response.status_code, 200)
