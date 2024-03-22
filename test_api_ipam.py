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

##### Tests Group

# PATCH /group

# POST /group

# DELETE /group/{groupId}

# GET /group/{groupId}
try:
    groupes = test_get('/group/1')[1]
    vannes = groupes[0]
    test = vannes == [1, 'Vannes']
except Exception as e:
    print(e)
    test = False
print(f'GET /group/{{groupId}} : {test}')

# GET /group/findByName
try:
    groupes = test_get('/group/findByName/', {'name':'Vannes'})[1]
    vannes = groupes[0]
    test = vannes == [1, 'Vannes']
except:
    test = False
print(f'GET /group : {test}')

# GET /group/findByParent

# GET /group/findByChild


##### Tests Address

# PATCH /address

# POST /address

# GET /address/findByAddress

# GET /address/{addressId}

# DELETE /address/{addressId}


##### Tests Subnet

# PATCH /subnet

# POST /subnet

# GET /subnet/findByAddress

# GET /subnet/findByMask

# GET /subnet/findByVlanid

# GET /subnet/{subnetId}

# DELETE /subnet/{subnetId}




# Test PUT /medal
#for couleur in ("bronze","silver"):
#    print(test_put('/medal/', {
#                    "medal_id": 1,
#                    "year": 2004,
#                    "color": couleur,
#                    "athlete_id": 14,
#                    "sport_id": 37
#                    }))