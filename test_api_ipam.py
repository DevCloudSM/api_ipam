import requests
import json
from requests.structures import CaseInsensitiveDict

def test_put(path:str='/', data:dict[str, str]= {}) -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.put( f'http://localhost:5000{path}', headers=headers, data=json.dumps(data))
    return (f'Code {test.status_code}', json.loads(test.text))

def test_get(path:str='/', data:dict[str, str]= {}) -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.get( f'http://localhost:5000{path}', headers=headers, data=json.dumps(data))
    return (f'Code {test.status_code}', json.loads(test.text))

def test_delete(path:str='/', id:int=0) -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.delete( f'http://localhost:5000{path}{id}', headers=headers)
    return (f'Code {test.status_code}', json.loads(test.text))

# Test GET /group/findByName
groupes = test_get('/group/findByName/', {'name':'Vannes'})[1]
vannes = groupes[0]
print(vannes)

# Test PUT /medal
#for couleur in ("bronze","silver"):
#    print(test_put('/medal/', {
#                    "medal_id": 1,
#                    "year": 2004,
#                    "color": couleur,
#                    "athlete_id": 14,
#                    "sport_id": 37
#                    }))