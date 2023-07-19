from playwright.sync_api import Page, expect

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
    # a_tag = page.locator("a")
    # expect(a_tag).to_have_text([
    #     ''
    # ])

# testing for tenant login page
def test_get_tenant_login(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/tenant_login")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        'Tenant Username: Charlotte', 
        'Tenant Username: Oli', 
        'Tenant Username: Nebiat', 
        'Tenant Username: Rich'
    ])



"""
test Get /landlord_dashboard/id
"""
# def test_get_landlord_dashboard_by_id(db_connection, page, test_web_address):
#     db_connection.seed("./seeds/airbnb_seeds.sql")
#     page.goto(f"http://{test_web_address}/landlord_login")
#     page.click("text=Landlord Username: Charlotte")

#     h1_element = page.locator("h1")
#     expect(h1_element).to_have_text("Welcome Charlotte")

"""
test GET /tenant_dashboard/id
"""
# def test_get_tenant_dashboard_by_id(db_connection, page, test_web_address):
#     db_connection.seed("./seeds/airbnb_seeds.sql")
#     page.goto(f"http://{test_web_address}/tenant_login")
#     page.click("text=Tenant Username: Oli")

#     h1_element = page.locator(".t-username")
#     expect(h1_element).to_have_text("Welcome Oli")


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
    expect(h2_tag).to_have_text("Sign out")

"""
test get /tenant_dashboard/{{tenant.id}}/spaces
click sign out, returns to tenant login page
"""

def test_sign_out_on_all_spaces_page(db_connection, page, test_web_address):
    db_connection.seed("./seeds/airbnb_seeds.sql")
    page.goto(f"http://{test_web_address}/tenant_dashboard/1/spaces")
    page.click("text=Sign out")

    # Add tests same as tenant login page


