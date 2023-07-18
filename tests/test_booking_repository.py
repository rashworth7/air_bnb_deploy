from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import datetime


"""
test create booking
updates booking list with a new booking
"""
def test_create_booking(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    booking_repo = BookingRepository(db_connection)
    booking_repo.create_booking(2, 3, 4, datetime(2023, 7, 18))
    all_bookings = booking_repo.all()
    assert all_bookings == [
        Booking(2, 2, 3, 4, "pending", datetime(2023, 7, 18))
    ]