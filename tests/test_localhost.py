#this is an example for error handling purposes. I need to update it so that it will pass under normal circumstances

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_click_target_element(driver):
    __tracebackhide__ = True  # Hides this function's source code from the output
    failure_message = None

    try:
        # 1. Navigate to the page
        driver.get("http://localhost:8000")
        # 2. Dismiss Cookie Popup (Optional)
        try:
            cookie_accept_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.ID, "accept-cookies-btn-id"))
            )
            cookie_accept_btn.click()
        except TimeoutException:
            pass
        # 3. Dismiss Marketing/Newsletter Popup (Optional)
        try:
            marketing_close_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "marketing-modal-close-class"))
            )
            marketing_close_btn.click()
        except TimeoutException:
            pass
        # 4. Click the main target element (Required)
        target_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "my-target-element-id"))
        )
        target_element.click()
    except Exception as e:
        raw_error = str(e)

        # Aggressively extract ONLY the specific error type
        if "net::" in raw_error:
            clean_error = "net::" + raw_error.split("net::")[1].split()[0]
        elif "Message: " in raw_error:
            clean_error = raw_error.split("Message: ")[1].split("\n")[0].strip()
        else:
            clean_error = raw_error.split("\n")[0]

        failure_message = f"Unexpected Failure: {clean_error}"

    # OUTSIDE the except block to avoid exception chaining
    if failure_message:
        # Fails the test (Red), but the pytrace=False argument hides the Python stack trace!
        pytest.fail(failure_message, pytrace=False)