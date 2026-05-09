#This is a series of examples I am currently using to base future front-end UI test on. These are not published yet, but I am hoping to do so shortly.  
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="function")
def driver():
    """
    Setup the Selenium WebDriver for Chrome.
    """
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Uncomment this to run tests invisibly in the background
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    yield driver
    
    # Clean up and close the browser after the test finishes
    driver.quit()


def test_login_form(driver):
    """
    Example 1: Interacting with a login form.
    Demonstrates locating input fields, sending keys, and clicking submit.
    """
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Locate username and password fields and enter credentials
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")
    
    # Click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Verify successful login by checking for the success flash message
    # We use an Explicit Wait to ensure the page has loaded the message
    flash_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
    assert "You logged into a secure area!" in flash_message.text


def test_dropdown_selection(driver):
    """
    Example 2: Selecting an option from a dropdown menu.
    Uses Selenium's built-in Select class to make interacting with <select> tags easy.
    """
    driver.get("https://the-internet.herokuapp.com/dropdown")
    
    # Locate the dropdown element
    dropdown_element = driver.find_element(By.ID, "dropdown")
    
    # Wrap it in the Select class
    select = Select(dropdown_element)
    
    # Select by visible text
    select.select_by_visible_text("Option 2")
    
    # Verify the selected option is correct
    selected_option = select.first_selected_option
    assert selected_option.text == "Option 2"


def test_handle_js_alert(driver):
    """
    Example 3: Handling JavaScript Alerts/Popups.
    Demonstrates how to switch from the main HTML context to a browser alert and accept it.
    """
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    
    # Click the button that triggers a JS Alert
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    
    # Wait for the alert to be present and switch to it
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    
    # Verify the text inside the alert popup
    assert alert.text == "I am a JS Alert"
    
    # Click 'OK' on the alert
    alert.accept()
    
    # Verify the result text on the page
    result = driver.find_element(By.ID, "result")
    assert result.text == "You successfully clicked an alert"


def test_hover_action(driver):
    """
    Example 4: Performing a mouse hover action.
    Uses ActionChains to simulate complex user gestures like hovering.
    """
    driver.get("https://the-internet.herokuapp.com/hovers")
    
    # Find the first user profile image
    user_avatar = driver.find_element(By.CSS_SELECTOR, ".figure")
    
    # The text we want to verify is hidden until we hover over the image
    hidden_text = user_avatar.find_element(By.CSS_SELECTOR, ".figcaption h5")
    assert not hidden_text.is_displayed()
    
    # Perform the hover action
    actions = ActionChains(driver)
    actions.move_to_element(user_avatar).perform()
    
    # Verify the text is now displayed after hovering
    assert hidden_text.is_displayed()
    assert hidden_text.text == "name: user1"


def test_explicit_wait_for_element(driver):
    """
    Example 5: Using Explicit Waits to handle dynamic content.
    This is crucial for modern web apps where elements load asynchronously (e.g., via AJAX).
    """
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    # Click the start button
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    
    # The loading bar appears and takes about 5 seconds to finish.
    # We wait up to 10 seconds for the "Hello World!" text to become visible in the DOM.
    # If it doesn't appear within 10 seconds, a TimeoutException is thrown.
    hello_world_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )
    
    assert hello_world_text.text == "Hello World!"
