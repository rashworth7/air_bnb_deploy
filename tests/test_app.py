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
    first_landlord_link = page.get_by_text('Charlotte')
    expect(first_landlord_link).to_have_attribute('href', '/landlord_dashboard/1')

# testing for tenant login page
def test_get_tenant_login(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/tenant_login")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        'Tenant Username: Charlotte', 
        'Tenant Username: Oli', 
        'Tenant Username: Nebiat', 
        'Tenant Username: Rich',
        'Back'
    ])
    second_tenant_link = page.get_by_text('Oli')
    expect(second_tenant_link).to_have_attribute('href', '/tenant_dashboard/2')

"""
test Get /landlord_dashboard/id
"""
def test_get_landlord_dashboard_by_id(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/landlord_login")
    page.click("text=Charlotte")

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
    
    # space_names = page.inner_text(".space_name")
    # for space_name in space_names:
    #     expect(space_name).not_to_be_empty()

def test_approve_changes_status_to_approved(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/landlord_listing/1")
    booking_repo = BookingRepository(db_connection)
    booking_id = 1
    booking = booking_repo.get_booking_by_id(booking_id)
    assert booking.status == "pending"

    button = page.locator(".approve-button")
    # button.click()

    # assert booking.status == "approved"



# def test_landlord_listing_navigation_back_to_dashboard(db_connection, page, test_web_address):
#     db_connection.seed("./seeds/airbnb_seeds.sql")
#     page.goto(f"http://{test_web_address}/landlord_listing/1")

#     page.click("text=Back to dashboard")
#     expect(page.url).to_be(f"http://{test_web_address}/landlord_dashboard/1")
#     expect(page.inner_text("h1")).to_contain("Welcome Charlotte")



"""
test GET /tenant_dashboard/id
"""
def test_get_tenant_dashboard_by_id(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/tenant_login")
    page.click("text=Oli")

    h1_element = page.locator(".t-username")
    expect(h1_element).to_have_text("Welcome Oli")
    li_tag = page.locator('li')
    expect(li_tag).to_have_text(["All spaces", "Requests"])
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Sign out")


"""
test get /tenant_dashboard/{{tenant.id}}/spaces
"""

def test_get_all_spaces(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/tenant_dashboard/1/spaces")
    expect(page).to_have_title("All spaces")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("All spaces")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(
        [
            "Find your dream stay",
            "Price per night: £50",
            "Click here to book!",
            "Price per night: £60",
            "Click here to book!",
            "Price per night: £20",
            "Click here to book!"
        ]
    )
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Back to dashboard")

"""
test get /tenant_dashboard/{{tenant.id}}/spaces
click sign out, returns to tenant login page
"""

def test_back_to_dashbpard_on_all_spaces_page(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/tenant_dashboard/2/spaces")
    page.click("text=Back to dashboard")

    h1_element = page.locator(".t-username")
    expect(h1_element).to_have_text("Welcome Oli")
    li_tag = page.locator('li')
    expect(li_tag).to_have_text(["All spaces", "Requests"])
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Sign out")


