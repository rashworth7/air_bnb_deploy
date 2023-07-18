from lib.tenant import Tenant

class TenantRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def list_tenants(self):
        rows = self._connection.execute('SELECT * from tenants')
        tenants = []
        for row in rows:
            item = Tenant(row['id'], row['username'])
            tenants.append(item)
        return tenants
    
    def get_tenant_by_id(self, id):
        rows = self._connection.execute('SELECT * from tenants where id=%s', [id])
        row = rows[0]
        tenant = Tenant(row['id'], row['username'])
        return tenant
