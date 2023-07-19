from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")

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