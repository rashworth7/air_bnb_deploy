from lib.availability_repository import AvailabilityRepository
from lib.availability import Availability
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import datetime


"""
test create booking
updates booking list with a new booking
checks all bookings are now updated
"""
def test_create_booking(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    booking_repo = BookingRepository(db_connection)
    booking = Booking(None, 3, 3, 2, None, "2023-07-18")
    booking_repo.create_booking(booking)
    all_bookings = booking_repo.all()
    assert all_bookings == [
        Booking(id=1, space_id=1, tenant_id=1, landlord_id=1, status='pending', date="2023-07-18"),
        Booking(id=2, space_id=1, tenant_id=1, landlord_id=1, status="approved", date="2023-07-17"),
        Booking(id=3, space_id=3, tenant_id=3, landlord_id=2, status="pending", date="2023-07-18")
    ]

"""
update booking changes status of the booking
depending on whether it is approved or denied
deny booking - no changes to availability table
"""

def test_deny_booking(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    booking_repo = BookingRepository(db_connection)
    booking_repo.update_booking(booking_id=1, approve_status=False)
    all_bookings = booking_repo.all()
    assert all_bookings == [
        Booking(id=2, space_id=1, tenant_id=1, landlord_id=1, status="approved", date="2023-07-17"),
        Booking(id=1, space_id=1, tenant_id=1, landlord_id=1, status='denied', date="2023-07-18")
    ]

"""
update booking changes status of the booking
depending on whether it is approved or denied
add a booking
deny booking - no changes to availability table
"""

def test_deny_booking_extra(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    booking_repo = BookingRepository(db_connection)
    booking = Booking(None, 3, 3, 2, None, "2023-07-18")
    booking_repo.create_booking(booking)
    booking_repo.update_booking(booking_id=3, approve_status=False)
    all_bookings = booking_repo.all()
    assert all_bookings == [
        Booking(id=1, space_id=1, tenant_id=1, landlord_id=1, status='pending', date="2023-07-18"),
        Booking(id=2, space_id=1, tenant_id=1, landlord_id=1, status="approved", date="2023-07-17"),
        Booking(id=3, space_id=3, tenant_id=3, landlord_id=2, status="denied", date="2023-07-18")
    ]

"""
get booking by id
"""
def test_get_booking_by_id(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    booking_repo = BookingRepository(db_connection)
    booking = booking_repo.get_booking_by_id(1)
    assert booking == Booking(id=1, space_id=1, tenant_id=1, landlord_id=1, status='pending', date="2023-07-18")

"""
approve a booking
removes that booking availability from the avilability table
"""

def test_approve_booking(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    booking_repo = BookingRepository(db_connection)
    booking_repo.update_booking(booking_id=1, approve_status="approved")
    all_bookings = booking_repo.all()
    assert all_bookings == [
        Booking(id=2, space_id=1, tenant_id=1, landlord_id=1, status="approved", date="2023-07-17"),
        Booking(id=1, space_id=1, tenant_id=1, landlord_id=1, status='approved', date="2023-07-18")
    ]

    availability_repo = AvailabilityRepository(db_connection)
    availability_repo.delete(1, "2023-07-18")
    availabilities = availability_repo.all()
    assert availabilities == [
        Availability(2, 1, '2023-07-19'),
        Availability(3, 1, '2023-07-20'),
        Availability(4, 2, '2023-07-21'),
        Availability(5, 2, '2023-07-22'),
        Availability(6, 2, '2023-07-23'),
        Availability(7, 3, '2023-07-24'),
    ]

"""
test get booking by status and landlord id. 
Check pending
"""

def test_booking_by_status_landlord_id(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    booking_repo = BookingRepository(db_connection)
    booking = Booking(None, 3, 3, 2, None, "2023-07-18")
    booking_repo.create_booking(booking)
    bookings = booking_repo.get_booking_by_status_and_landlord_id("pending", 2)
    assert bookings == [
        Booking(id=3, space_id=3, tenant_id=3, landlord_id=2, status="pending", date="2023-07-18")
    ]