
class Booking:
    
    def __init__(self, id, space_id, tenant_id, landlord_id, status, date):
        self.id = id
        self.space_id = space_id
        self.tenant_id = tenant_id
        self.landlord_id = landlord_id
        self.status = status
        self.date = date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Booking({self.id}, {self.space_id}, {self.tenant_id}, {self.landlord_id}, {self.status}, {self.date.strftime("%d/%m/%Y")})'
    
