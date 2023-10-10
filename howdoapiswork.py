import requests
import json


response = requests.get(f'https://api.api-ninjas.com/v1/jokes?limit={1}', headers={'X-Api-Key' : "FWIYfCodkizNPtWSfjMNYw==BpZw8KgtJ4foUCyJ"})

if response.status_code == requests.codes.ok:
    response = json.loads(response.text)
    print(response[0]['joke'])