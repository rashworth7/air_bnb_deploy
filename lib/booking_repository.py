from lib.booking import Booking

class BookingRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        pass

    def create_booking(self):
        pass

    def update_booking(self):
        #approve or deny booking
        #updates booking table
        pass

    def get_booking_by_status_and_landlord_id(self):
        pass