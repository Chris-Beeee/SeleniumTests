# Basic web UI verification test in selenium for python, using pyest and pycharm as an IDE
# Expected result from this is a FAIL. the element required does not exist on this page.
# Code generated via Google Antigravity using Gemini 3.1. It required substantial reworks to exception handling,
# reporting the results while avoiding stacktrace errors and cookie and marketing popups.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_click_target_element(driver):
    failure_message = None  # Error stored here to avoid chained stacktrace errors
    try:
        driver.get("http://localhost:8000")
        wait = WebDriverWait(driver, 10)
        # Dismiss popups
        try:
            popup_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".cm-btn.cm-btn-success.cm-btn-accept-all"))
            )
            driver.execute_script("arguments[0].click();", popup_btn)
        except Exception:
            pass
        try:
            popup2_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".cmpboxbtn.cmpboxbtnyes.cmptxt_btn_yes"))
            )
            driver.execute_script("arguments[0].click();", popup2_btn)
        except Exception:
            pass
            # Main Element Click
            target_classes_raw = "hover:underline focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-orange-500"
            css_selector = "." + target_classes_raw.replace(":", r"\:").replace(" ", ".")
            # 1. Wait for the element to exist and be clickable
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)),
                message=f"Timeout: The target element with classes '{target_classes_raw}' failed to appear."
            )

            # refresh element to avoid dynamic element re-rendering

            fresh_element = driver.find_element(By.CSS_SELECTOR, css_selector)
            driver.execute_script("arguments[0].click();", fresh_element)
    except Exception as e:
        # Extract the cleanest possible error string (Selenium stores it in e.msg)
        if hasattr(e, 'msg') and e.msg:
            clean_reason = e.msg
        else:
            clean_reason = str(e).split('\n')[0]

        failure_message = f"❌ TEST FAILED\nReason: {clean_reason}"
        # test pass/fail outside the try/except block

        if failure_message:
            pytest.fail(failure_message, pytrace=False)

