from playwright.sync_api import Page, expect
from lib.booking_repository import BookingRepository
# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")
    div_tag = page.locator("div")
    # landlord_anchor = page.locator("[id='landlord_login']")
    landlord_anchor = page.locator('#landlord_login')
    tenant_anchor = page.locator('#tenant_login')

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text(["This is the homepage.\n", 'Are you a?'])
    expect(div_tag).to_have_text("\n Landlord\n Tenant")
    expect(landlord_anchor).to_have_attribute("href", "/landlord_login")
    expect(tenant_anchor).to_have_attribute("href", "/tenant_login")

# testing for landlord login page
def test_get_landlord_login(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/landlord_login")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        'Landlord Username: Charlotte', 
        'Landlord Username: Oli', 
        'Landlord Username: Nebiat', 
        'Landlord Username: Rich'
    ])

"""
test Get /landlord_dashboard/id
"""
def test_get_landlord_dashboard_by_id(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/landlord_login")
    page.click("text=Landlord Username: Charlotte")

    h1_element = page.locator("h1")
    expect(h1_element).to_have_text("Welcome Charlotte")

"""
test GET landlord_listing/id
"""
def test_get_landlord_listing_by_id(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/landlord_dashboard/1")
    page.click("text=My Spaces and requests")

    h1_element = page.locator("h1")
    expect(h1_element).to_have_text("Your spaces, Charlotte")
    
    space_names = page.locator_all(".space_name")
    expect(len(space_names)).to_be(2)
    expect("Space 1").in_(space_names[0].inner_text())
    expect("Space 2").in_(space_names[1].inner_text())

def test_approve_changes_status_to_approved(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/landlord_listing/1")

    page.click("text=Approve")

    approved_booking = BookingRepository.get_booking_by_id(1)
    expect(approved_booking.status).to_equal('Approved')



def test_landlord_listing_navigation_back_to_dashboard(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/landlord_listing/1")

    page.click("text=Back to dashboard")
    expect(page.url).to_be(f"http://{test_web_address}/landlord_dashboard/1")
    expect(page.inner_text("h1")).to_contain("Welcome Charlotte")



"""
test GET /tenant_dashboard/id
"""
# def test_get_tenant_dashboard_by_id(db_connection, page, test_web_address):
#     db_connection.seed("./seeds/airbnb_seeds.sql")
#     page.goto(f"http://{test_web_address}/tenant_login")
#     page.click("text=Tenant Username: Oli")

#     h1_element = page.locator(".t-username")
#     expect(h1_element).to_have_text("Welcome Oli")