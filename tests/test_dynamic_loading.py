import pytest
from pages.herokuapp_pages import HerokuAppDynamicLoadingPage

def test_explicit_wait_for_element_to_render(driver):
    """
    Fleshed out example of explicit waits.
    This is the most crucial concept in UI testing: waiting for an element
    to appear in the DOM after an asynchronous operation (like an AJAX call).
    """
    page = HerokuAppDynamicLoadingPage(driver)
    page.open()
    
    # Start the loading process (which simulates a slow network request)
    page.start_loading()
    
    # The get_finish_text() method in the page object uses `self.find()`, 
    # which wraps `WebDriverWait(...).until(EC.presence_of_element_located(...))`.
    # This automatically pauses the test until the element exists, avoiding flakiness.
    finish_text = page.get_finish_text()
    
    assert finish_text == "Hello World!", f"Expected 'Hello World!', got '{finish_text}'"
