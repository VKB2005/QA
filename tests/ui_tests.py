import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_verify_website_title(driver):
    """
    Tests if the website loads and has the expected title. This is a basic
    check to ensure the correct page is being loaded.
    """
    driver.get("https://www.iamdave.ai/")
    # Assert that the title of the page contains the expected text
    assert "DaveAI" in driver.title, "The title of the page is not correct"

def test_navigation_to_about_page(driver):
    driver.get("https://www.iamdave.ai/")
    about_link = driver.find_element(By.LINK_TEXT, "About")
    driver.execute_script("arguments[0].click();", about_link)

    # WAIT up to 10 seconds for the URL to contain "about" BEFORE checking it
    WebDriverWait(driver, 10).until(EC.url_contains("about"))

    # Now that we've waited, this assertion will pass
    assert "about" in driver.current_url.lower(), "Navigation to About page failed"
    
def test_homepage_heading_present(driver):
    """
    Checks if the main heading (<h1>) element is present on the homepage
    and contains the expected text. This verifies key content is visible.
    """
    driver.get("https://www.iamdave.ai/")
    # Find the h1 element, which is typically the main heading
    heading = driver.find_element(By.TAG_NAME, "h1")
    # Assert that the element is displayed on the page
    assert heading.is_displayed(), "Main heading is not displayed"
    # Assert that the heading text contains the expected content
    assert "AI Agents for Enterprise" in heading.text, "Heading text is incorrect"