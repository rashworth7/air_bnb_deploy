from lib.landlord_repository import LandlordRepository
from lib.landlord import Landlord

"""
test landlord lists all landlords
"""

def test_list_landlords(db_connection):
    db_connection.seed("seeds/airbnb_seeds.sql")
    landlord_repo = LandlordRepository(db_connection)
    landlords = landlord_repo.list_landlords()
    assert landlords == [
        Landlord(1, "Charlotte"),
        Landlord(2, "Oli"),
        Landlord(3, "Nebiat"),
        Landlord(4, "Rich")
    ]

"""
test get landlord by ID
returns single landlord bassed on ID
"""
def test_get_landlord_by_id(db_connection):
    db_connection.seed("seeds/airbnb_seeds.sql")
    landlord_repo = LandlordRepository(db_connection)
    landlord = landlord_repo.get_landlord_by_id(1)
    assert landlord == Landlord(1, "Charlotte")