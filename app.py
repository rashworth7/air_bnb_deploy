import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.landlord_repository import LandlordRepository

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


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
