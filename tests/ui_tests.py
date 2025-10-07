import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """
    This fixture sets up the WebDriver before each test and quits it after.
    Using a fixture ensures a clean browser instance for every test.
    """
    # Setup: Initialize the Chrome WebDriver using webdriver-manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)  # Implicit wait for elements to appear
    yield driver
    # Teardown: Close the browser window
    driver.quit()

def test_verify_website_title(driver):
    """
    Tests if the website loads and has the expected title. This is a basic
    check to ensure the correct page is being loaded.
    """
    driver.get("https://www.iamdave.ai/")
    # Assert that the title of the page contains the expected text
    assert "I AM DAVE" in driver.title, "The title of the page is not correct"

def test_navigation_to_about_page(driver):
    """
    Tests a navigation flow by finding the 'About' link, clicking it,
    and then verifying that the URL has changed to the about page.
    """
    driver.get("https://www.iamdave.ai/")
    # Find the 'About' link by its visible text and click it
    about_link = driver.find_element(By.LINK_TEXT, "About")
    about_link.click()
    # Assert that the current URL contains '/about', indicating successful navigation
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
    assert "Solving the world's most meaningful problems" in heading.text, "Heading text is incorrect"