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

    def get_booking_by_id(self, booking_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id = %s', [booking_id])
        row = rows[0]
        return Booking(row['id'], row['space_id'], row['tenant_id'], row['landlord_id'], row['status'], row['date'].strftime("%Y-%m-%d"))
        

    def update_booking(self, booking_id, approve_status):
        #approve or deny booking
        #updates booking table
        if not approve_status:
            self._connection.execute("UPDATE bookings SET status = 'denied' WHERE id = %s", [booking_id])
        else:
            print('1************')
            self._connection.execute("UPDATE bookings SET status = 'approved' WHERE id = %s", [booking_id])
            booking = self.get_booking_by_id(booking_id)
            print('2************')
            self._connection.execute("DELETE FROM availability WHERE space_id = %s AND date = %s", [booking.space_id, booking.date])

    def get_booking_by_status_and_landlord_id(self, status, landlord_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE status = %s AND landlord_id = %s', [status, landlord_id])
        bookings = []
        for row in rows:
            booking = Booking(row['id'], row['space_id'], row['tenant_id'], row['landlord_id'], row['status'], row['date'].strftime("%Y-%m-%d"))
            bookings.append(booking)
        return bookings


     