import requests
import unittest
import json
from random import choice

DEFAULT_HEADER = 'application/json'

SUCCESS = 200
INCORRECT_HEADER = 400
ADDED = 201