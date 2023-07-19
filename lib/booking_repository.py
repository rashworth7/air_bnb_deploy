from lib.booking import Booking
from datetime import datetime

class BookingRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in rows:
            booking = Booking(row['id'], row['space_id'], row['tenant_id'], row['landlord_id'], row['status'], row['date'].strftime("%Y-%m-%d"))
            bookings.append(booking)
        return bookings

    def create_booking(self, booking):
        self._connection.execute('INSERT INTO bookings (space_id, tenant_id, landlord_id, status, date) VALUES (%s, %s, %s, %s, %s)', [booking.space_id, booking.tenant_id, booking.landlord_id, "pending", booking.date])
        

    def update_booking(self, booking_id, approve_status):
        #approve or deny booking
        #updates booking table
        self._connection.execute("UPDATE bookings SET status = 'denied' WHERE id = %s", [booking_id])

    def get_booking_by_status_and_landlord_id(self):
        pass