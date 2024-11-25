from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (mock database)
products = [
    {"id": 1, "product_id": "P001", "name": "Bashpika Thulasi (Premium) - 7ML", "description": "Herbal oil for immunity", "mrp": 120, "distributor_price": "69.64 + GST (12%) = 78"},
    {"id": 2, "product_id": "P002", "name": "Bashpika Thulasi (Premium) - 10ML", "description": "Herbal oil for immunity", "mrp": 170, "distributor_price": "98.66 + GST (12%) = 110"},
    {"id": 3, "product_id": "P003", "name": "Bashpika Thulasi (Premium) - 5ML", "description": "Herbal oil for immunity", "mrp": 100, "distributor_price": "58.04 + GST (12%) = 65"},
    {"id": 4, "product_id": "P004", "name": "Ashtamrutham Vayuguliga (1 NOS)", "description": "Traditional Ayurvedic tablet", "mrp": 30, "distributor_price": "5.36 + GST (12%) = 6"},
    {"id": 5, "product_id": "P005", "name": "Ashtamrutham Vayuguliga", "description": "Ayurvedic herbal formulation", "mrp": 30, "distributor_price": "18.90 + GST (12%) = 21"},
    {"id": 6, "product_id": "P006", "name": "Sarvanga Thailam (Body Care Oil)", "description": "Oil for full-body massage", "mrp": 150, "distributor_price": "80.36 + GST (12%) = 90"},
    {"id": 7, "product_id": "P007", "name": "Sukh Pain Relief Oil 100ml", "description": "Oil for pain relief (large bottle)", "mrp": 180, "distributor_price": "96.58 + GST (12%) = 108"},
    {"id": 8, "product_id": "P008", "name": "Sukh Pain Relief Oil 50ml", "description": "Oil for pain relief (medium bottle)", "mrp": 100, "distributor_price": "53.57 + GST (12%) = 60"},
    {"id": 9, "product_id": "P009", "name": "Sukh Pain Relief Oil 20ml", "description": "Oil for pain relief (small bottle)", "mrp": 50, "distributor_price": "29.02 + GST (12%) = 32.50"},
    {"id": 10, "product_id": "P010", "name": "Lemon Grass Oil", "description": "Aromatic essential oil", "mrp": 120, "distributor_price": "61.02 + GST (18%) = 72"},
    {"id": 11, "product_id": "P011", "name": "Eucalyptus Oil", "description": "Essential oil for respiratory health", "mrp": 100, "distributor_price": "50.85 + GST (18%) = 60"}
]

# GET: Retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# GET: Retrieve a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

# POST: Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    if "id" not in new_product or "name" not in new_product or "product_id" not in new_product:
        return jsonify({"error": "Invalid data"}), 400
    products.append(new_product)
    return jsonify(new_product), 201

# PUT: Update an existing product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        data = request.json
        product.update(data)
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

# DELETE: Remove a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [product for product in products if product["id"] != product_id]
    return jsonify({"message": "Product deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
