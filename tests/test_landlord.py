from lib.landlord import Landlord

"""
test landlord constructs correctly
"""
def test_landlord_constructs():
    landlord = Landlord(1, "test username")
    assert landlord.id == 1
    assert landlord.username == "test username"

"""
test landlord objects are equal when same attributes
"""
def test_landlord_objects_equal():
    landlord1 = Landlord(1, "test username")
    landlord2 = Landlord(1, "test username")
    assert landlord1 == landlord2

"""
test landlord formats correctly into
an easy to read string
"""

def test_landlord_formats():
    landlord = Landlord(1, "test username")
    assert str(landlord) == "Landlord(1, test username)"
