import os
from flask import Flask, request, render_template, redirect
from lib.availability_repository import AvailabilityRepository
from lib.booking import Booking
from lib.database_connection import get_flask_database_connection
from lib.landlord_repository import LandlordRepository
from lib.space_repository import SpaceRepository
from lib.tenant_repository import TenantRepository
from lib.space import Space
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

# GET /tenant_login
# Returns the tenant login page
@app.route('/tenant_login', methods=['GET'])
def get_tenant_login():
    connection = get_flask_database_connection(app)
    repository = TenantRepository(connection)
    all_tenants = repository.list_tenants()
    return render_template('tenant_login.html', tenants = all_tenants)


#GET /landlord_login/id
# landlord dashboard page
@app.route('/landlord_dashboard/<int:landlord_id>')
def get_landlord_dashboard(landlord_id):
    connection = get_flask_database_connection(app)
    repository = LandlordRepository(connection)
    landlord = repository.get_landlord_by_id(landlord_id)
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
@app.route('/tenant_dashboard/<int:tenant_id>')
def get_tenant_dashboard(tenant_id):
    connection = get_flask_database_connection(app)
    repository = TenantRepository(connection)
    tenant = repository.get_tenant_by_id(tenant_id)
    return render_template('/tenant_dashboard.html', tenant=tenant)

# GET /tenant_dashboard/{{tenant.id}}/spaces
# All spaces on tenant route
@app.route('/tenant_dashboard/<int:tenant_id>/spaces')
def get_all_spaces(tenant_id):
    connection = get_flask_database_connection(app)
    tenant_repository = TenantRepository(connection)
    spaces_repository = SpaceRepository(connection)
    tenant = tenant_repository.get_tenant_by_id(tenant_id)
    spaces = spaces_repository.all()
    return render_template('all_spaces.html', tenant=tenant, spaces=spaces)


# GET //tenant_dashboard/{{tenant.id}}/spaces/{{space_id}}
# Dsiplay page with option to book a space
# Shows dates available

@app.route('/tenant_dashboard/<int:tenant_id>/spaces/<int:space_id>')
def get_single_space(tenant_id, space_id):
    connection = get_flask_database_connection(app)
    tenant_repository = TenantRepository(connection)
    spaces_repository = SpaceRepository(connection)
    availability_repository = AvailabilityRepository(connection)
    tenant = tenant_repository.get_tenant_by_id(tenant_id)
    space = spaces_repository.get_space_by_id(space_id)
    availabilities = availability_repository.get_space_by_id_and_tenant_id(space_id, tenant_id)
    return render_template('book_space.html', tenant=tenant, space=space, availabilities=availabilities)

"""
Clicking the book button on the space page
refreshes the page removing the date
updates the available dates table
Adds a booking to booking table for review
"""
@app.route('/book/<space_id>/<space_title>/<landlord_id>/<tenant_id>/<date>', methods=['POST'])
def post_book_space(space_id, space_title, landlord_id, tenant_id, date):
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    booking = Booking(None, space_id, space_title, tenant_id, landlord_id, None, date)
    booking_repository.create_booking(booking)
    return redirect(request.referrer)
    
# GET /tenant_dashboard/{{tenant.id}}/requests
# all requests on tenant route
@app.route('/tenant_dashboard/<int:tenant_id>/requests')
def get_tenant_requests(tenant_id):
    connection = get_flask_database_connection(app)
    tenant_repo = TenantRepository(connection)
    tenant = tenant_repo.get_tenant_by_id(tenant_id)
    booking_repo = BookingRepository(connection)
    tenant_bookings = booking_repo.get_booking_by_tenant_id(tenant_id)
    return render_template('tenant_requests.html', tenant=tenant, bookings=tenant_bookings)


# GET /landlord_dashboard/{{landlord.id}}/create_a_space
# render the create space form
@app.route('/landlord_dashboard/<int:landlord_id>/create_a_space')
def get_create_a_space(landlord_id):
    connection = get_flask_database_connection(app)
    landlord_repo = LandlordRepository(connection)
    landlord = landlord_repo.get_landlord_by_id(landlord_id)
    return render_template('/create_a_space.html', landlord = landlord)

# POST /landlord_dashboard/{{landlord.id}}/create_a_space
# create_space on landlord id
@app.route('/create_space/<int:landlord_id>', methods=['POST'])
def post_create_a_space(landlord_id):
    title = request.form['title']
    description = request.form['description']
    price_per_night = request.form['price per night']
    availability_date = request.form['available dates']
    connection = get_flask_database_connection(app)
    # use input from form to pass in to Space()
    a_space = Space(None, title, description, price_per_night, landlord_id)
    spaces_repository = SpaceRepository(connection)
    space_id = spaces_repository.create_space(a_space)
    availability_repo = AvailabilityRepository(connection)
    availability_repo.create(space_id, availability_date)
    return redirect(f'/landlord_spaces_and_requests/{landlord_id}')
    

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


