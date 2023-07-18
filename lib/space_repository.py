from lib.space import Space


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            space = Space(row['id'], row['title'], row['description'], row['price_per_night'], row['landlord_id'])
            spaces.append(space)
        return spaces

    def get_space_by_id(self, space_id):
        pass

    def get_spaces_by_landlord_id(self, landlord_id):
        pass

    def create_space(self, space):
        self._connection.execute('INSERT INTO spaces (title, description, price_per_night, landlord_id) VALUES (%s, %s, %s, %s)', [space.title, space.description, space.price_per_night, space.landlord_id])

    def request_space(self, space_id, date, tenant_id, landlord_id):
        pass