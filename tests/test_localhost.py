import pytest
from pages.giantbomb_page import GiantBombPage

# Expected result from this is a FAIL because localhost:8000 probably isn't running GiantBomb
def test_click_target_element(driver):
    failure_message = None
    try:
        page = GiantBombPage(driver)
        
        # Override URL for this specific test
        page.URL = "http://localhost:8000"
        page.open()
        
        # Dismiss popups
        page.dismiss_popups()
        
        # Click target element
        page.click_target_element()
        
    except Exception as e:
        if hasattr(e, 'msg') and e.msg:
            clean_reason = e.msg
        else:
            clean_reason = str(e).split('\n')[0]

        failure_message = f"❌ TEST FAILED\nReason: {clean_reason}"

    if failure_message:
        pytest.fail(failure_message, pytrace=False)
