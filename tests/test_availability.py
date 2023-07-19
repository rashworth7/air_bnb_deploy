from lib.availability import Availability

"""
test constructs correctly
"""

def test_constructs():
    availability = Availability(1, 1, "2023-06-01")
    assert availability.id == 1
    assert availability.space_id == 1
    assert availability.date == "2023-06-01"

def test_equal_objects():
    availability1 = Availability(1, 1, "2023-06-01")
    availability2 = Availability(1, 1, "2023-06-01")
    assert availability1 == availability2

def test_string_formats():
    availability = Availability(1, 1, "2023-06-01")
    assert str(availability) == "Availability(1, 2023-06-01)"