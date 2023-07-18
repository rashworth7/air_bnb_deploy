class Space:
    def __init__(self, id, title, description, price_per_night, landlord_id, availability_dates):
        self.id = id
        self.title = title
        self.description = description
        self.price_per_night = price_per_night
        self.landlord_id = landlord_id
        self.availability_dates = availability_dates

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Space({self.id}, {self.title}, {self.description}, {self.price_per_night}, {self.landlord_id}, {self.availability_dates})"
