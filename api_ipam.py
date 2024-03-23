from flask import Flask, request, jsonify
import python_sql as ps
import front_ipam

api_ipam = Flask(__name__)

@api_ipam.route("/")
def menu():
    return front_ipam.yaml()

#Group
# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/group", methods = ['GET','POST','PATCH'])
def slash_group():
    if request.method == 'POST':
        return "<h2>POST group</h2>"
    if request.method == 'PATCH':
        return "<h2>PATCH group</h2>"
    return "<h1>GET Group</h1>"

# Code fait !
@api_ipam.route("/group/<int:groupId>", methods = ['GET','DELETE'])
def slash_group_groupId(groupId):
    if request.method == 'DELETE':
        return f"<h2>DELETE Group n°{groupId}</h2>"
    groupe = ps.get(['group'], 'id', groupId)
    return jsonify(groupe)

# Code fait !
@api_ipam.route("/group/findByName/", methods = ['GET'])
def slash_group_findByName():
    name = request.get_json()['name']
    groupes = ps.get(['group'], 'name', name)
    return jsonify(groupes)

# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/group/findByParent", methods = ['GET'])
def slash_group_findByParent():
    return "<h1>GET Group findByParent</h1>"

# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/group/findByChild", methods = ['GET'])
def slash_group_findByChild():
    return "<h1>GET Group findByChild</h1>"

#Address
# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/address/", methods = ['GET','POST','PATCH'])
def slash_address():
    if request.method == 'POST':
        return "<h2>POST address</h2>"
    if request.method == 'PATCH':
        return "<h2>PATCH address</h2>"
    return "<h1>GET address</h1>"

# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/address/<int:addressId>", methods = ['GET','DELETE'])
def slash_address_addressId(addressId):
    if request.method == 'DELETE':
        return f"<h2>DELETE address n°{addressId}</h2>"
    return f"<h1>GET address n°{addressId}</h1>"

# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/address/findByAddress", methods = ['GET'])
def slash_address_findByAddress():
    return "<h1>GET address findByAdress</h1>"

#Subnet
# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/subnet/", methods = ['GET','POST','PATCH'])
def slash_subnet():
    if request.method == 'POST':
        return "<h2>POST subnet</h2>"
    if request.method == 'PATCH':
        return "<h2>PATCH subnet</h2>"
    return "<h1>GET subnet</h1>"

# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/subnet/<int:subnetId>", methods = ['GET','DELETE'])
def slash_subnet_subnetId(subnetId):
    if request.method == 'DELETE':
        return f"<h2>DELETE subnet n°{subnetId}</h2>"
    return f"<h1>GET subnet n°{subnetId}</h1>"

# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/subnet/findByName", methods = ['GET'])
def slash_subnet_findByName():
    return "<h1>GET subnet findByName</h1>"

# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/subnet/findByParent", methods = ['GET'])
def slash_subnet_findByParent():
    return "<h1>GET subnet findByParent</h1>"

# Code à faire, dont il faut rédiger un test, dont le test ne fonctionne pas
@api_ipam.route("/subnet/findByChild", methods = ['GET'])
def slash_subnet_findByChild():
    return "<h1>GET subnet findByChild</h1>"

if __name__ == "__main__":
    api_ipam.run(debug=True)