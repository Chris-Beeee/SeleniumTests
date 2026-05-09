import pytest
from pages.herokuapp_pages import HerokuAppDropdownPage

def test_select_option_1(driver):
    """
    Fleshed out example of interacting with a native HTML <select> dropdown.
    """
    page = HerokuAppDropdownPage(driver)
    page.open()
    
    # Select the first option
    page.select_option("Option 1")
    
    # Verify the selection was recorded
    assert page.get_selected_option() == "Option 1", "Option 1 was not selected successfully"

def test_select_option_2(driver):
    """
    Test selecting a different option to ensure the dropdown isn't hardcoded.
    """
    page = HerokuAppDropdownPage(driver)
    page.open()
    
    # Select the second option
    page.select_option("Option 2")
    
    # Verify the selection
    assert page.get_selected_option() == "Option 2", "Option 2 was not selected successfully"
