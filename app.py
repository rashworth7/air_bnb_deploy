import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.landlord_repository import LandlordRepository
from lib.tenant_repository import TenantRepository

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


