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

if __name__ == '__main__':
    unittest.main(verbosity=2)