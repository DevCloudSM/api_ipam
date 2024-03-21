"""Ce test ne fonctionne pas mais permet de se faire une idée d'à quoi ressemble un fichier test"""




import requests
import json
from requests.structures import CaseInsensitiveDict

r = requests.put('http://localhost:5000/medal/', data={'test':'test'})

def test_put(path:str='/', data:dict[str, str]= {}) -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.put( f'http://localhost:5000{path}', headers=headers, data=json.dumps(data))
    return (test.status_code == 200, json.loads(test.text))

def test_get(path:str='/', data:dict[str, str]= {}) -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.get( f'http://localhost:5000{path}', headers=headers, data=json.dumps(data))
    return (test.status_code == 200, json.loads(test.text))

def test_delete(path:str='/', id:int=0) -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.delete( f'http://localhost:5000{path}{id}', headers=headers)
    return (test.status_code == 200, json.loads(test.text))

# Test GET /medal
print(test_get('/medal/'))

# Test PUT /medal
for couleur in ("bronze","silver"):
    print(test_put('/medal/', {
                    "medal_id": 1,
                    "year": 2004,
                    "color": couleur,
                    "athlete_id": 14,
                    "sport_id": 37
                    }))
