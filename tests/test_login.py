import pytest
from pages.herokuapp_pages import HerokuAppLoginPage

def test_valid_login(driver):
    """
    Fleshed out example of testing a valid login scenario.
    Verifies that providing correct credentials logs the user in successfully.
    """
    page = HerokuAppLoginPage(driver)
    page.open()
    
    # Perform login with known good credentials
    page.login("tomsmith", "SuperSecretPassword!")
    
    # Verify the success flash message appears
    flash_text = page.get_flash_message()
    assert "You logged into a secure area!" in flash_text, f"Expected success message, got: {flash_text}"

def test_invalid_login(driver):
    """
    Example of a negative test case for the login form.
    Verifies that incorrect credentials trigger the proper error message.
    """
    page = HerokuAppLoginPage(driver)
    page.open()
    
    # Attempt login with bad credentials
    page.login("invalid_user", "wrong_password")
    
    # Verify the error flash message appears
    flash_text = page.get_flash_message()
    assert "Your username is invalid!" in flash_text, f"Expected error message, got: {flash_text}"
