import pytest
from pages.herokuapp_pages import HerokuAppHoverPage

def test_hover_action_reveals_text(driver):
    """
    Fleshed out example of using ActionChains to perform complex interactions like hovering.
    This test verifies that hidden text becomes visible only after moving the mouse over an element.
    """
    page = HerokuAppHoverPage(driver)
    page.open()
    
    # Get the hidden text element before doing anything
    hidden_text = page.get_hidden_text_element()
    
    # 1. Verify the text is initially hidden from the user
    assert not hidden_text.is_displayed(), "Text should be hidden before hovering"
    
    # 2. Perform the mouse hover action
    page.hover_over_avatar()
    
    # 3. Verify the text is now displayed
    assert hidden_text.is_displayed(), "Text should be visible after hovering"
    
    # 4. Verify the content of the revealed text
    assert hidden_text.text == "name: user1", f"Unexpected hidden text: {hidden_text.text}"
