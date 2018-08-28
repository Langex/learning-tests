import requests
import unittest
import json
from random import choice

DEFAULT_HEADER = 'application/json'

SUCCESS = 200
INCORRECT_HEADER = 400
ADDED = 201

FIRST_NAME = ('Frodo', 'Bilbo', 'Gandalf', 'Samwise', 'Meriadoc', 'Peregrin')
LAST_NAME = ('Baggins', 'Baggins', 'the Grey', 'Gamgee', 'Brandybuck', 'Took')
DESCRIPTION = ('ring bearer', 'burglar', 'wizard', 'gardener', 'pony rider', 'pipe smoker')

class TestEmployees(unittest.TestCase):

	def __init__(self, *a, **kw):
		super(TestEmployees, self).__init__(*a, **kw)
		self.host = 'localhost:8080'
		self.command = 'employees'
		self.url = 'http://{}/api/{}'.format(self.host, self.command)

	def test_employees_creation(self):
		random_first_name = "{}".format(choice(FIRST_NAME))
		random_last_name = "{}".format(choice(LAST_NAME))
		description = "{}".format(choice(DESCRIPTION))
		kwargs = {'firstName': random_first_name, 'lastName': random_last_name, 'description': description}
		status_employees, text = self._create_employees(**kwargs)
		self.assertEqual(status_employees, ADDED)

	def _create_employees(self, firstName, lastName, description, headers=DEFAULT_HEADER):
		_headers = {'content-type': headers}
		_payload = json.dumps({'firstName': firstName, 'lastName': lastName, 'description': description})
		_response = requests.post(self.url, data=_payload, headers=_headers)
		return _response.status_code, _response.json()


if __name__ == '__main__':
	unittest.main(verbosity=2)