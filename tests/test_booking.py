from lib.booking import Booking
from datetime import datetime

"""
test booking constructs correctly
"""
def test_booking_constructs():
    booking = Booking(1, 2, 3, 4, "pending", datetime(2023, 7, 18))
    assert booking.id == 1
    assert booking.space_id == 2
    assert booking.tenant_id == 3
    assert booking.status == "pending"
    assert booking.date == datetime(2023, 7, 18)

"""
test booking class are equal
when they have the same attributes
"""
def test_equal_booking_objects():
    booking1 = Booking(1, 2, 3, 4, "pending", datetime(2023, 7, 18))
    booking2 = Booking(1, 2, 3, 4, "pending", datetime(2023, 7, 18))
    assert booking1 == booking2

"""
test booking formats into a nice string
"""
def test_booking_formats_correctly():
    booking = Booking(1, 2, 3, 4, "pending", datetime(2023, 7, 18))
    assert str(booking) == "Booking(1, 2, 3, 4, pending, 18/07/2023)"