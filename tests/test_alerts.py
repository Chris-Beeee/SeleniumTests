import pytest
from pages.herokuapp_pages import HerokuAppAlertPage

def test_handle_js_alert(driver):
    """
    Fleshed out example of handling browser-level JavaScript alerts.
    Since these aren't in the DOM, Selenium has to switch context to them.
    """
    page = HerokuAppAlertPage(driver)
    page.open()
    
    # Trigger the JS Alert
    page.trigger_alert()
    
    # Switch to the alert, read its text, and accept (click OK) it
    alert_text = page.get_alert_text_and_accept()
    
    # Verify the text inside the alert was correct
    assert alert_text == "I am a JS Alert", f"Unexpected alert text: {alert_text}"
    
    # Verify the page updated to reflect the alert was accepted
    result_text = page.get_result_text()
    assert result_text == "You successfully clicked an alert", f"Unexpected result text: {result_text}"
