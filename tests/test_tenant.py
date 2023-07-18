from lib.tenant import Tenant

# test construction
def test_tenant_construction():
    a_tenant = Tenant(1, 'MyUsername')
    assert a_tenant.id == 1
    assert a_tenant.username == 'MyUsername'

# test equality 
def test_equality_between_objects():
    a_tenant = Tenant(1, 'MyUsername')
    b_tenant = Tenant(1, 'MyUsername')
    assert a_tenant == b_tenant

# test formatting in string
def test_string_formatting():
    a_tenant = Tenant(1, 'MyUsername')
    assert str(a_tenant) == 'Tenant(1, MyUsername)'