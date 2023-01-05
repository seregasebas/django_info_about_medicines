import requests
import pprint

# response = requests.get('http://127.0.0.1:8000/api/v1/druggroups/', auth = ('german', 'maximgerman1$'))
# pprint.pprint(response.json())

token = 'a8c93abb4066a7c62e9ca99540cbb705bcd28e4e'
headers = {'Authorization':f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v1/druggroups/', headers=headers)
#response = requests.get('http://127.0.0.1:8000/api/v1/druggroups/')
pprint.pprint(response.json())
