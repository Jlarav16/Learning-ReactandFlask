from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'
mongo = PyMongo(app)

CORS(app)

dbProducts = mongo.db.products
dbUsers = mongo.db.users

@app.route('/', methods=['GET'])
def products():
    products = list()
    for product in dbProducts.find():
        products.append({
            '_id': str(ObjectId(product['_id'])),
            'name_product': product['name_product'],
            'quantity': product['quantity'],
            'price': product['price'],
            'description': product['description'],
            'total': product['total'],
        })

    return jsonify(products)


@app.route('/products', methods=['POST'])
def create():
    id = dbProducts.insert({
        'name_product': request.json['name_product'],
        'quantity': request.json['quantity'],
        'price': request.json['price'],
        'description': request.json['description'],
        'total': request.json['total']
    })
    print(request.json)
    print(str(ObjectId(id)))
    return jsonify(str(ObjectId(id)))


@app.route('/products/<id>', methods=['PUT'])
def update(id):
    dbProducts.update_one({'_id': ObjectId(id)}, {'$set': {
            'name_product': request.json['name_product'],
            'quantity': request.json['quantity'],
            'price': request.json['price'],
            'description': request.json['description'],
            'total': request.json['total']
        }})
    
    return '<h1> I\'m Updating the product with id: '+id


@app.route('/products/<id>', methods=['DELETE'])
def delete(id):
    dbProducts.delete_one({'_id': ObjectId(id)})
    return '<h1> I\'m Deleting the product with id: '+id


@app.route('/users', methods=['POST'])
def createUser():
    id = dbUsers.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    })
    print(str(ObjectId(id)))
    return jsonify(str(ObjectId(id)))


@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in dbUsers.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'password': doc['password']
        })
    return jsonify(users)


@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    print(id)
    user = dbUsers.find_one({'_id': ObjectId(id)})
    print(user)
    return jsonify({
        '_id': str(ObjectId(user['_id'])),
        'name': user['name'],
        'email': user['email'],
        'password': user['password']})


@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    print(id)
    dbUsers.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'users deleted'})


@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    print(id)
    print(request.json)
    dbUsers.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    }})
    return jsonify({'msg': 'User Updated'})


if __name__ == "__main__":
    app.run(debug=True)
