from lib.space import Space

"""
test constructs
"""

def test_space_constructs():
    space = Space(1, 'test title', 'test description', 'test price', 'test owner id', 'test availability')
    assert space.id == 1
    assert space.title == 'test title'
    assert space.description == 'test description'
    assert space.price_per_night == 'test price'
    assert space.owner_id == 'test owner id'
    assert space.availability_dates == 'test availability'

"""
test equality
"""

def test_space_equality():
        space1 = Space(1, 'test title', 'test description', 'test price', 'test owner id', 'test availability')
        space2 = Space(1, 'test title', 'test description', 'test price', 'test owner id', 'test availability')
        assert space1 == space2

"""
formats nicely
"""

def test_format_to_string():
      space = Space(1, 'test title', 'test description', 'test price', 'test owner id', 'test availability')
      assert str(space) == "Space(1, test title, test description, test price, test owner id, test availability)"