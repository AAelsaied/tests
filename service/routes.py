@app.route('/api/products/<int:id>/', methods=['GET'])
def read_product(id):
    product = Product.query.get(id)
    return jsonify(product.to_dict())
@app.route('/api/products/<int:id>/', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    product.update(request.json)
    db.session.commit()
    return jsonify(product.to_dict())
@app.route('/api/products/<int:id>/', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204
@app.route('/api/products/', methods=['GET'])
def list_products():
    query = Product.query
    if request.args.get('name'):
        query = query.filter_by(name=request.args['name'])
    if request.args.get('category'):
        query = query.filter_by(category=request.args['category'])
    if request.args.get('availability'):
        query = query.filter_by(availability=request.args['availability'])
    products = query.all()
    return jsonify([product.to_dict() for product in products])
