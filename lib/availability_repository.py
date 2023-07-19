from lib.availability import Availability

class AvailabilityRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM availability')
        availabilities = []
        for row in rows:
            availability = Availability(row['id'], row['space_id'], row['date'].strftime("%Y-%m-%d"))
            availabilities.append(availability)
        return availabilities
    
    def create(self, space_id, date):
        self._connection.execute('INSERT INTO availability (space_id, date) VALUES (%s, %s)', [space_id, date])

    def delete(self, availability_id):
        self._connection.execute('DELETE FROM availability WHERE id = %s', [availability_id])

    def get_by_space_id(self, space_id):
        rows = self._connection.execute('SELECT * FROM availability WHERE space_id = %s', [space_id])
        availabilities = []
        for row in rows:
            availability = Availability(row['id'], row['space_id'], row['date'].strftime("%Y-%m-%d"))
            availabilities.append(availability)
        return availabilities
    