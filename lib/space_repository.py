class SpaceRepository:
    pass

    def all_spaces(self):
        pass

    def get_space_by_id(self, space_id):
        pass

    def get_spaces_by_landlord_id(self, landlord_id):
        pass

    def create_space(self, title, description, price_per_night, landlord_id, availability_dates, booked_dates):
        pass

    def request_space(self, space_id, date, tenant_id, landlord_id):
        pass