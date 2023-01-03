import requests
import pprint

response = requests.get('http://127.0.0.1:8000/contacts/contacts/')

pprint.pprint(response.json())