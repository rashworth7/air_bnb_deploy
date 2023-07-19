class Availability:
    
    def __init__(self, id, space_id, date):
        self.id = id
        self.space_id = space_id
        self.date = date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Availability({self.space_id}, {self.date})"