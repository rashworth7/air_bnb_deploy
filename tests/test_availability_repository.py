from lib.availability import Availability
from lib.availability_repository import AvailabilityRepository

"""
test all returns all
"""
def test_all(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    availability_repo = AvailabilityRepository(db_connection)
    availability_dates_spaces = availability_repo.all()
    assert availability_dates_spaces == [
        Availability(1, 1, '2023-07-18'),
        Availability(2, 1, '2023-07-19'),
        Availability(3, 1, '2023-07-20'),
        Availability(4, 2, '2023-07-21'),
        Availability(5, 2, '2023-07-22'),
        Availability(6, 2, '2023-07-23'),
        Availability(7, 3, '2023-07-24'),
    ]

"""
create availability inserts new row into
availability_of_spaces table
check with all method
"""

def test_create(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    availability_repo = AvailabilityRepository(db_connection)
    availability_repo.create(1, '2024-10-10')
    availability_dates_spaces = availability_repo.all()
    assert availability_dates_spaces == [
        Availability(1, 1, '2023-07-18'),
        Availability(2, 1, '2023-07-19'),
        Availability(3, 1, '2023-07-20'),
        Availability(4, 2, '2023-07-21'),
        Availability(5, 2, '2023-07-22'),
        Availability(6, 2, '2023-07-23'),
        Availability(7, 3, '2023-07-24'),
        Availability(8, 1, '2024-10-10'),
    ]

"""
delete a date
removes from table
"""

def test_delete(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    availability_repo = AvailabilityRepository(db_connection)
    availability_repo.delete(4)
    availability_dates_spaces = availability_repo.all()
    assert availability_dates_spaces == [
        Availability(1, 1, '2023-07-18'),
        Availability(2, 1, '2023-07-19'),
        Availability(3, 1, '2023-07-20'),
        Availability(5, 2, '2023-07-22'),
        Availability(6, 2, '2023-07-23'),
        Availability(7, 3, '2023-07-24'),
    ]

"""
get by space id
returns list of availability objects
"""

def test_get_by_space_id(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    availability_repo = AvailabilityRepository(db_connection)
    availabilities = availability_repo.get_by_space_id(1)
    assert availabilities == [
        Availability(1, 1, '2023-07-18'),
        Availability(2, 1, '2023-07-19'),
        Availability(3, 1, '2023-07-20'),
    ]