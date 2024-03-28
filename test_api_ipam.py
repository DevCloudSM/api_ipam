import requests
import json
from requests.structures import CaseInsensitiveDict
import traceback

def test_patch(path:str='/', data:dict[str, str]= {}) -> tuple[str, dict]:
    try:
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = 'application/json'
        test = requests.patch( f'http://localhost:5000{path}', headers=headers, data=json.dumps(data))
        return (f'Code {test.status_code}', json.loads(test.text))
    except:
        return traceback.print_exc()

def test_get(path:str='/') -> tuple[str, dict]:
    try:
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = 'application/json'
        test = requests.get( f'http://localhost:5000{path}', headers=headers)
        return (f'Code {test.status_code}', json.loads(test.text))
    except:
        return traceback.print_exc()

def test_delete(path:str='/', id:int=0) -> tuple[str, dict]:
    try:
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = 'application/json'
        test = requests.delete( f'http://localhost:5000{path}{id}', headers=headers)
        return (f'Code {test.status_code}', json.loads(test.text))
    except:
        return traceback.print_exc()

def test_post(path:str='/', data:dict[str, str]= {}) -> tuple[str, dict]:
    try:
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = 'application/json'
        test = requests.post( f'http://localhost:5000{path}', headers=headers, data=json.dumps(data))
        return (f'Code {test.status_code}', json.loads(test.text))
    except:
        return traceback.print_exc()

##### Tests Group
def test_group():
    # POST /group
    t_post = test_post('/group/', {'id':2,
                                    'name':'Vannes',
                                    'parent_id':1,
                                    'content_ids':[1,2,3,4],
                                    'reading_roles':['dsi_local', 'superadmin'],
                                    'writing_roles':['superadmin']})
    print(f'POST /group/ {{data}} : {t_post}')

    # PATCH /group
    t_patch = test_patch('/group/2', {'id':2,
                                    'name':'Vannes',
                                    'parent_id':1,
                                    'content_ids':[5,6,7,8],
                                    'reading_roles':['dsi_local', 'superadmin'],
                                    'writing_roles':['superadmin']})
    print(f'PATCH /group/{{groupId}} {{data}} : {t_patch}')

    # GET /group/{groupId}
    t_get = test_get('/group/2')
    print(f'GET /group/{{groupId}} : {t_get}')

    # GET /group/findByName
    t_get_findbyName = test_get('/group/findByName?name=Vannes')
    print(f'GET /group/findByName?name=Vannes : {t_get_findbyName}')

    # GET /group/findByParent
    t_get_findbyParent = test_get('/group/findByParent?parent=1')
    print(f'GET /group/findByParent?parent=1 : {t_get_findbyParent}')

    # GET /group/findByChild
    t_get_findbyChild = test_get('/group/findByChild?child=6')
    print(f'GET /group/findByChild?child=6 : {t_get_findbyChild}')

    # DELETE /group/{groupId}
    t_delete = test_delete('/group/', 2)
    print(f'DELETE /group/id : {t_delete}')

##### Tests Address
def test_address():
    # POST /address
    t_post = test_post('/address/', {'id':4,
                                    'address':'10.0.0.1',
                                    'mask':25,
                                    'online':False,
                                    'attribuated':True})
    print(f'POST /address/ {{data}} : {t_post}')
    # PATCH /address
    t_patch = test_patch('/address/4', {'id':4,
                                    'address':'10.0.0.2',
                                    'mask':24,
                                    'online':True,
                                    'attribuated':True})
    print(f'PATCH /address/{{addressId}} {{data}} : {t_patch}')

    # GET /address/findByAddress
    t_get_findByAddress = test_get('/group/findByAddress?address=10.0.0.2')
    print(f'GET /group/findByAddress?address=10.0.0.2 : {t_get_findByAddress}')

    # GET /address/{addressId}
    t_get = test_get('/address/2')
    print(f'GET /address/{{addressId}} : {t_get}')

    # DELETE /address/{addressId}
    t_delete = test_delete('/address/', 2)
    print(f'DELETE /address/id : {t_delete}')

##### Tests Subnet
def test_subnet():
    # POST /subnet
    t_post = test_post('/subnet/',{'id':7,
                                    '1st_address':'10.0.0.0',
                                    'last_address':'10.0.0.4',
                                    'description':"Range Wifi de Brest",
                                    'mask':32,
                                    'reading_roles':["dsi_local","superadmin"],
                                    'writing_roles':["superadmin"],
                                    'group_id':3})
    print(f'POST /subnet/ {{data}} : {t_post}')

    # PATCH /subnet
    t_patch = test_post('/subnet/7',{'id':7,
                                    '1st_address':'10.0.0.0',
                                    'last_address':'10.0.0.4',
                                    'description':"Range Wifi de Vannes",
                                    'mask':32,
                                    'reading_roles':["dsi_local","superadmin"],
                                    'writing_roles':["superadmin"],
                                    'group_id':3})
    print(f'PATCH /subnet/{{subnetId}} {{data}} : {t_patch}')

    # GET /subnet/findByAddress
    t_get_findByAddress = test_get('/subnet/findByAddress?address=10.0.0.2')
    print(f'GET /subnet/findByAddress?address=10.0.0.2 : {t_get_findByAddress}')

    # GET /subnet/findByMask
    t_get_findByAddress = test_get('/subnet/findByMask?mask=32')
    print(f'GET /subnet/findByMask?mask=32 : {t_get_findByAddress}')

    # GET /subnet/findByVlanid
    t_get_findByAddress = test_get('/subnet/findByVlanid?vlanid=3')
    print(f'GET /subnet/findByAddress?vlanid=3 : {t_get_findByAddress}')

    # GET /subnet/{subnetId}
    t_get = test_get('/subnet/7')
    print(f'GET /subnet/{{subnetId}} : {t_get}')

    # DELETE /subnet/{subnetId}
    t_delete = test_delete('/subnet/', 7)
    print(f'DELETE /subnet/id : {t_delete}')

if __name__ == '__main__':
    print("Test Address".center(34, '='))
    test_address()
    print("Test Group".center(34, '='))
    test_group()
    print("Test Subnet".center(34, '='))
    test_subnet()