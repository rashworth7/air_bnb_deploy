from lib.landlord import Landlord

class LandlordRepository:
    
    def __init__(self, connection) -> None:
        self._connection = connection

    def list_landlords(self):
        rows = self._connection.execute('SELECT * FROM landlords')
        landlords = []
        for row in rows:
            landlord = Landlord(row['id'], row['username'])
            landlords.append(landlord)
        return landlords

    def get_landlord_by_id(self, landlord_id):
        row = self._connection.execute('SELECT * FROM landlords WHERE id = %s', [landlord_id])
        return Landlord(row[0]['id'], row[0]['username'])