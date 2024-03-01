from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

# Initialize Flask application
app = Flask(__name__)

# Initialize Flask HTTP Basic Auth
auth = HTTPBasicAuth()

# SQLite configuration - change the path to your desired location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Vehicle model
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placas = db.Column(db.String(20))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

# Create the database tables
with app.app_context():
    db.create_all()

# Sample user credentials (for demonstration purposes only)
users = {
    "admin": "123123"
}

# Authentication function
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# Root route - requires authentication
@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')

# Route to add a new vehicle
@app.route('/api/vehicles', methods=['POST'])
@auth.login_required
def add_vehicle():
    # Check if request is in JSON format and contains required fields
    if not request.json or 'id' not in request.json or 'placas' not in request.json or 'lat' not in request.json or 'lon' not in request.json:
        abort(400)  # Bad request
    data = request.json
    # Check if a vehicle with the same ID already exists
    existing_vehicle = Vehicle.query.filter_by(id=data['id']).first()
    if existing_vehicle:
        abort(409)  # Conflict: Vehicle with the same ID already exists
    # Create a new Vehicle object and add it to the database
    vehicle = Vehicle(id=data['id'], placas=data['placas'], lat=data['lat'], lon=data['lon'])
    db.session.add(vehicle)
    db.session.commit()
    # Return JSON response with details of the added vehicle
    return jsonify({'vehicle': {'id': vehicle.id, 'placas': vehicle.placas, 'lat': vehicle.lat, 'lon': vehicle.lon}}), 200

# Route to update an existing vehicle
@app.route('/api/vehicles/<int:vehicle_id>', methods=['PUT'])
@auth.login_required
def update_vehicle(vehicle_id):
    # Retrieve the vehicle by its ID
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        abort(404)  # Vehicle not found
    # Check if request is in JSON format
    if not request.json:
        abort(400)  # Bad request
    data = request.json
    # Update vehicle attributes with data from the request
    vehicle.placas = data.get('placas', vehicle.placas)
    vehicle.lat = data.get('lat', vehicle.lat)
    vehicle.lon = data.get('lon', vehicle.lon)
    db.session.commit()
    # Return JSON response with updated vehicle details
    return jsonify({'vehicle': {'id': vehicle.id, 'placas': vehicle.placas, 'lat': vehicle.lat, 'lon': vehicle.lon}}), 200

# Route to delete a vehicle by its ID
@app.route('/api/vehicles/<int:vehicle_id>', methods=['DELETE'])
@auth.login_required
def delete_vehicle(vehicle_id):
    # Retrieve the vehicle by its ID
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        abort(404)  # Vehicle not found
    # Delete the vehicle from the database
    db.session.delete(vehicle)
    db.session.commit()
    # Return success message
    return jsonify({'result': True}), 200

# Route to get all vehicles
@app.route('/api/vehicles')
@auth.login_required
def get_vehicles():
    # Retrieve all vehicles from the database
    vehicles = Vehicle.query.all()
    # Create a list of dictionaries containing vehicle details
    vehicle_data = [{'id': vehicle.id, 'placas': vehicle.placas, 'lat': vehicle.lat, 'lon': vehicle.lon} for vehicle in vehicles]
    # Return JSON response with the list of vehicles
    return jsonify(vehicle_data), 200

# Main entry point
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)

