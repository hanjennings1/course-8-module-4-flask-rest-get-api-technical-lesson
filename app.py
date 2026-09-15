from flask import Flask, jsonify, request

app = Flask(__name__)


# Mock product data (acts as our "database")
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]


@app.route("/")
def home():
    # Simple welcome message for the root endpoint
    return jsonify({"message": "Welcome to the Product Catalog API!"})

@app.route("/products", methods=["GET"])
def get_products():
    # Optional query param, e.g. /products?category=books
    category = request.args.get("category")
    if category:
        # Filter products by category (case-insensitive match)
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered), 200
    # No filter provided — return all products
    return jsonify(products), 200

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    # Find the first product matching the given id, else None
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return jsonify(product), 200
    # No match found — return 404 with an error message
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    # Run the app in debug mode (auto-reload + detailed error pages)
    app.run(debug=True)