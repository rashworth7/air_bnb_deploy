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
        self._connection.execute('INSERT INTO availability (space_id, date) SELECT %s, %s WHERE NOT EXISTS (SELECT (space_id, date) FROM availability WHERE space_id = %s AND date = %s)', [space_id, date, space_id, date])

    def delete(self, space_id, date):
        self._connection.execute('DELETE FROM availability WHERE space_id = %s AND date = %s', [space_id, date])

    def get_by_space_id(self, space_id):
        rows = self._connection.execute('SELECT * FROM availability WHERE space_id = %s', [space_id])
        availabilities = []
        for row in rows:
            availability = Availability(row['id'], row['space_id'], row['date'].strftime("%Y-%m-%d"))
            availabilities.append(availability)
        return availabilities


    def get_space_by_id_and_tenant_id(self, space_id, tenant_id):
        rows = self._connection.execute('SELECT * FROM availability WHERE space_id = %s', [space_id])
        availabilities = []
        for row in rows:
            availability = Availability(row['id'], row['space_id'], row['date'].strftime("%Y-%m-%d"))
            availabilities.append(availability)

        # pending availabilities
        rows = self._connection.execute('SELECT availability.id, availability.space_id, availability.date FROM availability JOIN spaces on availability.space_id = spaces.id JOIN bookings on bookings.date = availability.date WHERE tenant_id = %s AND spaces.id = %s;', [tenant_id, space_id])
        pending_availabilities = []
        for row in rows:
            availability = Availability(row['id'], row['space_id'], row['date'].strftime("%Y-%m-%d"))
            pending_availabilities.append(availability)

        tenant_availabilities = [x for x in availabilities if x not in pending_availabilities]

        return tenant_availabilities