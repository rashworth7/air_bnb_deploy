from lib.space import Space

"""
test constructs
"""

def test_space_constructs():
    space = Space(1, 'test title', 'test description', 'test price', 'test landlord id')
    assert space.id == 1
    assert space.title == 'test title'
    assert space.description == 'test description'
    assert space.price_per_night == 'test price'
    assert space.landlord_id == 'test landlord id'

"""
test equality
"""

def test_space_equality():
        space1 = Space(1, 'test title', 'test description', 'test price', 'test landlord id')
        space2 = Space(1, 'test title', 'test description', 'test price', 'test landlord id')
        assert space1 == space2

"""
formats nicely
"""

def test_format_to_string():
    space = Space(1, 'test title', 'test description', 'test price', 'test landlord id')
    assert str(space) == "Space(1, test title, test description, test price, test landlord id)"

