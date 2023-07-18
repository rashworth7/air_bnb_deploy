from lib.tenant_repository import TenantRepository
from lib.tenant import Tenant

# test listing of tenants usernames - for tenant login page
def test_list_all_tenants_usernames(db_connection):
    db_connection.seed('seeds/airbnb_seeds.sql')
    repository = TenantRepository(db_connection)
    all_tenants = repository.list_tenants()
    assert all_tenants == [
        Tenant(1, 'Charlotte'),
        Tenant(2, 'Oli'),
        Tenant(3, 'Nebiat'),
        Tenant(4, 'Rich')
    ]
