from playwright.sync_api import Page

@pytest.mark.parametrize("myname, myemail, mycompany", [
    ("Juan", "juan@email.com", "Companyex1"),
    ("Ana", "ana@email.com", "Companyex2"),
    ("Pedro", "pedro@email.com", "Companyex3"),
])
def test_loggin(page: Page, myname, myemail, mycompany):
    page.goto("https://www.assaia.com/#")
    
    #page.locator(".btn_label", has_text="Get in touch").click()
    #page.locator(".btn_primary", has_text="Get in touch").click()
    page.get_by_role("main").get_by_role("link", name="Get in touch").click()
    assert page.get_by_role("heading", name="Send us a message").inner_text() == "Send us a message"

    #name, Email Address, Company
    page.locator("[name='name']").fill(myname) 
    page.locator("[name='email']").fill(myemail)
    page.locator("[name='Company']").fill(mycompany)  

    page.get_by_text("Submit").click()

    page.wait_for_selector("text=Please confirm you're not a robot")
    assert page.get_by_text("Please confirm you're not a robot").is_visible()