# Technical Lesson: REST & GET APIs with Flask

**Completed Sept 15, 2026**

This lesson has been completed. The Flask GET API described below has been implemented in `app.py`, tested against all listed endpoints, and follows the RESTful conventions outlined in this README.

## Learning Goals

- [x] Understand the purpose of RESTful APIs and HTTP GET methods.
- [x] Build basic Flask routes that respond to GET requests.
- [x] Return structured JSON data from API endpoints.
- [x] Use query parameters to filter responses.
- [x] Follow RESTful conventions in route naming and response structure.

## Introduction

REST (Representational State Transfer) is a widely used architectural style for designing APIs that interact with web resources. The GET method is the foundation for retrieving data in any RESTful service.

This lesson focused on:

- Building GET routes with Flask.
- Returning mock product data in JSON format.
- Supporting query parameters for filtered responses.
- Following best practices for RESTful design.

The example used was a product catalog API. This API allows users to:

- View a full list of available products.
- Request a specific product by its ID.
- Filter products by category using a query string.

The system:

- Uses static mock data to simulate a real backend.
- Implements route handlers that return properly formatted responses.

This lesson built a working GET API step by step, laying the groundwork for full CRUD operations in later lessons.

## What Was Built

### Setting Up the Project

The project was cloned and dependencies were installed.

If using `pipenv`:

```bash
git clone <repo-url>
cd flask-rest-get-api
pipenv install
```

If using `pip`:

```bash
git clone <repo-url>
cd flask-rest-get-api
pip install -r requirements.txt
```

### The GET API — `app.py`

All routes are defined in `app.py`, simulating a product catalog with mock data.

```python
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
```

### Testing the API

The app was run with:

```bash
python app.py
```

And verified against the following endpoints:

| Endpoint | Description | Verified |
|---|---|---|
| `http://localhost:5000/` | Welcome message | ✅ |
| `http://localhost:5000/products` | All products | ✅ |
| `http://localhost:5000/products/2` | Product with ID 2 | ✅ |
| `http://localhost:5000/products?category=books` | Filtered by category | ✅ |

Testing was performed using the browser, Postman, and curl.

## Best Practices Applied

- Used nouns for resource routes (`/products` instead of `/getProducts`).
- Returned JSON responses with appropriate HTTP status codes (200, 404).
- Kept GET requests safe and idempotent — no data was modified.
- Validated and normalized query parameters to prevent case mismatches.
- Followed REST conventions for scalability and readability.

## Conclusion

This lesson is complete. By building a RESTful GET API in Flask, this project demonstrates:

- Serving consistent, structured data to client applications.
- A scalable route structure that follows RESTful standards.
- Simulated real-world backend functionality ahead of database integration.
- A foundation for more advanced API actions like POST, PATCH, and DELETE in upcoming lessons.

## 
**Next steps:** extend this API with full CRUD operations (POST, PATCH, DELETE) in the following module.