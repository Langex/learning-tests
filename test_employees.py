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

	def test_delete(self):
		rezult = self._get_employees()
		print('rezult: "' + str(rezult) + '"')
		identificator = choice(rezult)
		print('identificator: "' + str(identificator) + '"')
		status_code, text = self._delete_employees(self.url, identificator)
		self.assertEqual(status_code, SUCCESS)
		self.assertNotIn(identificator, self._get_employees('href'))

	def _create_employees(self, firstName, lastName, description, headers=DEFAULT_HEADER):
		_headers = {'content-type': headers}
		_payload = json.dumps({'firstName': firstName, 'lastName': lastName, 'description': description})
		_response = requests.post(self.url, data=_payload, headers=_headers)
		return _response.status_code, _response.json()

	def _delete_employees(self, identificator):
		_response = requests.delete("{}/{}".format(self.url, identificator))
		return _response.status_code, _response.json()

	def _get_employees(self, identificator=None):
		_url = self.url
		if identificator:
			_url = "{}/{}".format(self.url, identificator)
		print('_url: "' + str(_url) + '"')
		_response = requests.get(_url)
		return _response.status_code, _response.json()

	def _get_employees_id(self):
		_url = self.url
		_response = requests.get(_url)
		return _response.status_employees, _response.json()


	def _get_ids(self, msg):
		req = json.loads(msg)
		ids = []

		for el in req['_embedded']['employees']:

			href = el['_links']['self']['href']
			ident = href.split('/')[-1]
			ids.append(ident)
			
			print('href: ' + str(ident))
			print('ids: ' + str(ids))

		return ids

	# def _get_list_of(self, key):
	# 	_, data = self._get_employees()
	# 	return map(lambda x: x.get(key), data.get('employees'))

if __name__ == '__main__':
	unittest.main(verbosity=2)