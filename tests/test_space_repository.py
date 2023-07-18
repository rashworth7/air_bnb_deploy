from lib.space import Space 
from lib.space_repository import SpaceRepository

"""
when we call the all method we get a list of space objects(db starts empty)
"""
def test_all_method(db_connection):
    db_connection.seed("seeds/airbnb_seeds.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()

    assert spaces == [
        Space(1, 'Space 1', 'Space 1 is very nice', 50, 1),
        Space(2, 'Space 2', 'Space 2 is cool', 60, 1),
        Space(3, 'Space 3', 'Space 3 rubbish', 20, 2)
    ]

"""
when we call create we get a new space in the list
"""
def test_create_method(db_connection):
    db_connection.seed("seeds/airbnb_seeds.sql")
    repository = SpaceRepository(db_connection)

    repository.create_space(Space(None, 'Cozy Space', 'Coziest space ever!', 120, 3))

    spaces = repository.all()

    assert spaces == [
                Space(1, 'Space 1', 'Space 1 is very nice', 50, 1),
                Space(2,'Space 2', 'Space 2 is cool', 60, 1),
                Space(3,'Space 3', 'Space 3 rubbish', 20, 2),
                Space(4, 'Cozy Space', 'Coziest space ever!', 120, 3)
    ]
