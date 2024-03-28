import requests
import json
from requests.structures import CaseInsensitiveDict
import traceback

def test_patch(path:str='/', data:dict[str, str]= {}) -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.patch( f'http://localhost:5000{path}', headers=headers, data=json.dumps(data))
    return (f'Code {test.status_code}', json.loads(test.text))

def test_get(path:str='/') -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.get( f'http://localhost:5000{path}', headers=headers)
    return (f'Code {test.status_code}', json.loads(test.text))

def test_delete(path:str='/', id:int=0) -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.delete( f'http://localhost:5000{path}{id}', headers=headers)
    return (f'Code {test.status_code}', json.loads(test.text))

def test_post(path:str='/', data:dict[str, str]= {}) -> tuple[bool, dict]:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/json'
    test = requests.post( f'http://localhost:5000{path}', headers=headers, data=json.dumps(data))
    return (f'Code {test.status_code}', json.loads(test.text))

##### Tests Group

# POST /group
try:
    t_post = test_post('/group/', {'id':2,
                                   'name':'Vannes',
                                   'parent_id':1,
                                   'content_ids':[1,2,3,4],
                                   'reading_roles':['dsi_local', 'superadmin'],
                                   'writing_roles':['superadmin']})
    print(f'POST /group/ {"{data}"} : {t_post}')
except Exception as e:
    traceback.print_exc()

# PATCH /group

# GET /group/{groupId}
try:
    groupes = test_get('/group/2')[1]
    vannes = groupes[0]
    test = vannes == [1, 'Vannes']
except Exception as e:
    print(e)
    test = False
print(f'GET /group/{{groupId}} : {test}')

# GET /group/findByName
try:
    groupes = test_get('/group/findByName?name=Vannes')[1]
    vannes = groupes[0]
    test = vannes == [1, 'Vannes']
except:
    test = False
print(f'GET /group : {test}')

# GET /group/findByParent

# GET /group/findByChild

# DELETE /group/{groupId}
try:
    t_delete = test_delete('/group/', 2)
    print(f'DELETE /group/id : {t_delete}')
except Exception as e:
    traceback.print_exc()

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