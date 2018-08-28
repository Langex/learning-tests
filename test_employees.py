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