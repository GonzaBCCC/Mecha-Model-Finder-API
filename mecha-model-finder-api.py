# Import necessary modules from Flask and other libraries
from flask import Flask, jsonify, request, url_for
from flask_cors import CORS
import json

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for the entire application to allow cross-origin requests from the front-end
CORS(app)

# --- Mock Database ---
# This is a simple in-memory list of dictionaries to act as our database.
# In a real-world application, you would use a proper database like PostgreSQL or MongoDB.
kits = [
    {
        "id": 1,
        "name": "RX-78-2 Gundam",
        "series": "Mobile Suit Gundam",
        "scale": "1/144",
        "manufacturer": "Bandai",
        "release_year": 1980,
        "price_usd": 15.00,
        "image_url": "https://placehold.co/400x400/000000/FFFFFF?text=RX-78-2",
    },
    {
        "id": 2,
        "name": "Char's Zaku II",
        "series": "Mobile Suit Gundam",
        "scale": "1/100",
        "manufacturer": "Bandai",
        "release_year": 2000,
        "price_usd": 45.00,
        "image_url": "https://placehold.co/400x400/FF0000/FFFFFF?text=Zaku+II",
    },
    {
        "id": 3,
        "name": "Thousand Sunny",
        "series": "One Piece",
        "scale": "Non-Scale",
        "manufacturer": "Bandai",
        "release_year": 2010,
        "price_usd": 30.00,
        "image_url": "https://placehold.co/400x400/00FF00/000000?text=Thousand+Sunny",
    },
    {
        "id": 4,
        "name": "Evangelion Unit-01",
        "series": "Neon Genesis Evangelion",
        "scale": "1/400",
        "manufacturer": "Kotobukiya",
        "release_year": 2021,
        "price_usd": 65.00,
        "image_url": "https://placehold.co/400x400/8A2BE2/FFFFFF?text=Evangelion",
    },
    {
        'id': 5,
        'name': 'Gundam Astray Red Frame',
        'series': 'Gundam',
        'scale': '1/100',
        'manufacturer': 'Bandai',
        'release_year': 2019,
        'price': 35.50,
        'image_url': 'https://placehold.co/200x200/e5e7eb/4b5563?text=Astray+Red+Frame'
    },
    {
        'id': 6,
        'name': 'Strike Freedom Gundam',
        'series': 'Gundam Seed',
        'scale': '1/60',
        'manufacturer': 'Bandai',
        'release_year': 2022,
        'price': 150.00,
        'image_url': 'https://placehold.co/200x200/e5e7eb/4b5563?text=Strike+Freedom+Gundam'
    },

]

# A simple counter to generate unique IDs for new kits
next_id = 5

# --- API Endpoints ---

# The base URL, returning a welcome message and a list of available endpoints.
@app.route("/", methods=["GET"])
def home():
    """
    Handles the home route, providing a welcome message and links to main endpoints.
    """
    return jsonify({
        "message": "Welcome to the DIY Anime Model Kit API!",
        "available_endpoints": {
            "get_all_kits": url_for("get_all_kits"),
            "search_kits_by_series_or_scale": url_for("get_all_kits", series="Gundam", scale="1/144"),
            "get_kit_by_id_example": url_for("get_kit_by_id", kit_id=1),
            "create_kit": url_for("create_kit"),
            "update_kit_example": url_for("update_kit", kit_id=1),
            "delete_kit_example": url_for("delete_kit", kit_id=1),
        }
    })

# GET method: Retrieves a list of all anime model kits or filters by series and/or scale.
@app.route("/kits", methods=["GET"])
def get_all_kits():
    """
    Retrieves a list of all anime model kits or filters by series and/or scale.
    Example usage:
    - GET /kits
    - GET /kits?series=Mobile Suit Gundam
    - GET /kits?scale=1/144
    - GET /kits?series=Mobile Suit Gundam&scale=1/144
    """
    series_filter = request.args.get("series")
    scale_filter = request.args.get("scale")

    filtered_kits = kits

    # Filter by series if the 'series' parameter is provided
    if series_filter:
        filtered_kits = [kit for kit in filtered_kits if kit["series"].lower() == series_filter.lower()]

    # Filter by scale if the 'scale' parameter is provided
    if scale_filter:
        filtered_kits = [kit for kit in filtered_kits if kit["scale"].lower() == scale_filter.lower()]

    # Return the filtered list of kits
    return jsonify(filtered_kits)

# GET method: Retrieves detailed information for a single kit by its ID.
@app.route("/kits/<int:kit_id>", methods=["GET"])
def get_kit_by_id(kit_id):
    """
    Retrieves detailed information for a single kit by its ID.
    Example usage:
    - GET /kits/1
    """
    # Find the kit with the matching ID
    kit = next((k for k in kits if k["id"] == kit_id), None)

    # If the kit is found, return its data
    if kit:
        return jsonify(kit)

    # If the kit is not found, return a 404 Not Found error
    return jsonify({"error": "Kit not found"}), 404

# POST method: Creates a new kit.
@app.route("/kits", methods=["POST"])
def create_kit():
    """
    Creates a new kit.
    Expects a JSON payload in the request body.
    Example JSON:
    {
        "name": "Gundam Exia",
        "series": "Mobile Suit Gundam 00",
        "scale": "1/100",
        "manufacturer": "Bandai",
        "release_year": 2007,
        "price_usd": 30.00,
        "image_url": "https://placehold.co/400x400/0000FF/FFFFFF?text=Exia"
    }
    """
    global next_id

    # Check if the request body is valid JSON
    if not request.json:
        return jsonify({"error": "Invalid JSON"}), 400

    # Create the new kit dictionary and assign a new ID
    new_kit = {
        "id": next_id,
        "name": request.json.get("name"),
        "series": request.json.get("series"),
        "scale": request.json.get("scale"),
        "manufacturer": request.json.get("manufacturer"),
        "release_year": request.json.get("release_year"),
        "price_usd": request.json.get("price_usd"),
        "image_url": request.json.get("image_url"),
    }

    # Add the new kit to our mock database
    kits.append(new_kit)

    # Increment the ID counter for the next kit
    next_id += 1

    # Return the newly created kit with a 201 Created status code
    return jsonify(new_kit), 201

# PUT method: Updates an existing kit by its ID.
@app.route("/kits/<int:kit_id>", methods=["PUT"])
def update_kit(kit_id):
    """
    Updates an existing kit by its ID.
    Expects a JSON payload in the request body with the fields to update.
    Example usage:
    - PUT /kits/1
    Example JSON:
    {
        "price_usd": 18.00
    }
    """
    # Find the kit with the matching ID
    kit = next((k for k in kits if k["id"] == kit_id), None)

    # If the kit is not found, return a 404 Not Found error
    if not kit:
        return jsonify({"error": "Kit not found"}), 404

    # Check if the request body is valid JSON
    if not request.json:
        return jsonify({"error": "Invalid JSON"}), 400

    # Update the kit's fields from the request JSON
    kit.update(request.json)

    # Return the updated kit
    return jsonify(kit)

# DELETE method: Deletes a kit by its ID.
@app.route("/kits/<int:kit_id>", methods=["DELETE"])
def delete_kit(kit_id):
    """
    Deletes a kit by its ID.
    Example usage:
    - DELETE /kits/1
    """
    global kits

    # Find the kit to delete
    kit_to_delete = next((k for k in kits if k["id"] == kit_id), None)

    # If the kit is not found, return a 404 Not Found error
    if not kit_to_delete:
        return jsonify({"error": "Kit not found"}), 404

    # Remove the kit from the list
    kits = [k for k in kits if k["id"] != kit_id]

    # Return a success message
    return jsonify({"message": f"Kit with id {kit_id} deleted successfully"})

# This section is for running the app.
if __name__ == "__main__":
    # Make sure you have the Flask-CORS library installed by running
    # pip install Flask-CORS
    app.run(debug=True)
