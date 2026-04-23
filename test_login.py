from playwright.sync_api import Page
import pytest

@pytest.mark.parametrize("myname, myemail, mycompany", [
    ("Juan", "juan@email.com", "Companyex1"),
    ("Ana", "ana@email.com", "Companyex2"),
    ("Pedro", "pedro@email.com", "Companyex3"),
])
def test_login(page: Page, myname, myemail, mycompany):
    page.goto("https://www.assaia.com/#")
    
    page.get_by_role("main").get_by_role("link", name="Get in touch").click()

    page.locator("[name='name']").fill(myname) 
    page.locator("[name='email']").fill(myemail)
    page.locator("[name='Company']").fill(mycompany)  

    page.get_by_text("Submit").click()

    page.wait_for_selector("text=Please confirm you're not a robot")
    assert page.get_by_text("Please confirm you're not a robot").is_visible()