#This test is expected fo fail with a 'clean' error message
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_click_target_element(driver):
    __tracebackhide__ = True
    failure_message = None

    try:
        driver.get("http://localhost:8000")

        try:
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "popup-close-btn-id"))
            )
            close_button.click()
        except Exception:
            pass
        target_element = driver.find_element(By.ID, "my-target-element-id")
        target_element.click()
    except Exception as e:
        raw_error = str(e)

        # Aggressively extract ONLY the specific error type (e.g. net::ERR_CONNECTION_REFUSED or NoSuchElement)
        if "net::" in raw_error:
            # Grabs just the net::... part
            clean_error = "net::" + raw_error.split("net::")[1].split()[0]
        elif "Message: " in raw_error:
            # Grabs whatever is right after "Message:"
            clean_error = raw_error.split("Message: ")[1].split("\n")[0].strip()
        else:
            clean_error = raw_error.split("\n")[0]

        failure_message = clean_error

    if failure_message:
        pytest.xfail(failure_message)