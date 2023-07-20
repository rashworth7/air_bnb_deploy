import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.landlord_repository import LandlordRepository
from lib.tenant_repository import TenantRepository
from lib.space_repository import SpaceRepository
from lib.booking_repository import BookingRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# GET /landlord_login
# Returns the landlord login page
@app.route('/landlord_login', methods=['GET'])
def get_landlord_login():
    connection = get_flask_database_connection(app)
    repository = LandlordRepository(connection)
    all_landlords = repository.list_landlords()
    return render_template('landlord_login.html', landlords = all_landlords)


#GET /landlord_login/id
# landlord dashboard page
@app.route('/landlord_dashboard/<int:id>')
def get_landlord_dashboard(id):
    connection = get_flask_database_connection(app)
    repository = LandlordRepository(connection)
    landlord = repository.get_landlord_by_id(id)
    return render_template('/landlord_dashboard.html', landlord=landlord)

#GET /landlord_listing/id
@app.route('/landlord_spaces_and_requests/<int:landlord_id>')
def get_landlord_listing(landlord_id):
    connection = get_flask_database_connection(app)
    landlord_repo = LandlordRepository(connection)
    space_repo = SpaceRepository(connection)
    booking_repo = BookingRepository(connection)
    landlord = landlord_repo.get_landlord_by_id(landlord_id)
    landlord_spaces = space_repo.get_spaces_by_landlord_id(landlord_id)
    landlord_requests = booking_repo.get_booking_by_status_and_landlord_id('pending', landlord_id)
    return render_template('landlord_spaces_and_requests.html', landlord=landlord, spaces=landlord_spaces, requests=landlord_requests)

#POST /landlord_spaces_and_requests APPROVE request
@app.route('/approve_booking/<int:booking_id>', methods=['POST'])
def approve_booking(booking_id):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.update_booking(booking_id, approve_status=True)
    return redirect(request.referrer)

#POST /landlord_and_spaces_requests DENY request
@app.route('/deny_booking/<int:booking_id>', methods=['POST'])
def deny_booking(booking_id):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.update_booking(booking_id, approve_status=False)
    return redirect(request.referrer)

#GET /tenant_login/id
# tenant dashboard page
@app.route('/tenant_dashboard/<int:id>')
def get_tenant_dashboard(id):
    connection = get_flask_database_connection(app)
    repository = TenantRepository(connection)
    tenant = repository.get_tenant_by_id(id)
    return render_template('/tenant_dashboard.html', tenant=tenant)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


