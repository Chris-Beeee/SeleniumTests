#This is a series of examples I am currently using to base future front-end UI test on. These are not published yet, but I am hoping to do so shortly.  
import pytest
from pages.herokuapp_pages import (
    HerokuAppLoginPage,
    HerokuAppDropdownPage,
    HerokuAppAlertPage,
    HerokuAppHoverPage,
    HerokuAppDynamicLoadingPage
)

def test_login_form(driver):
    page = HerokuAppLoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in page.get_flash_message()


def test_dropdown_selection(driver):
    page = HerokuAppDropdownPage(driver)
    page.open()
    page.select_option("Option 2")
    assert page.get_selected_option() == "Option 2"


def test_handle_js_alert(driver):
    page = HerokuAppAlertPage(driver)
    page.open()
    page.trigger_alert()
    
    alert_text = page.get_alert_text_and_accept()
    assert alert_text == "I am a JS Alert"
    assert page.get_result_text() == "You successfully clicked an alert"


def test_hover_action(driver):
    page = HerokuAppHoverPage(driver)
    page.open()
    
    hidden_text = page.get_hidden_text_element()
    assert not hidden_text.is_displayed()
    
    page.hover_over_avatar()
    
    assert hidden_text.is_displayed()
    assert hidden_text.text == "name: user1"


def test_explicit_wait_for_element(driver):
    page = HerokuAppDynamicLoadingPage(driver)
    page.open()
    page.start_loading()
    
    assert page.get_finish_text() == "Hello World!"
