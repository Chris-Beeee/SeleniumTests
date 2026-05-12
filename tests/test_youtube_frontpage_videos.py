#This test is for a user who is not signed in to youtube, meaning there are several steps to get the site to display any videos at all
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


def test_youtube_video_titles():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.youtube.com/")

        # 1. Handle Cookies
        try:
            accept_button_selector = 'button[aria-label*="Accept the use of cookies"]'
            cookie_accept = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, accept_button_selector))
            )
            cookie_accept.click()
            print("Cookie banner found and accepted.")
            time.sleep(1)
        except TimeoutException:
            print("No cookie banner appeared (this is normal depending on region/session).")
        # 2. Find Search Box
        # We use the name attribute which is currently the most robust way to find it on YouTube
        search_selector = 'input[name="search_query"]'
        search_box_found = True

        try:
            search_box = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, search_selector))
            )
            print("Found search box. Searching for 'trending' to bypass history screen...")
            search_box.send_keys("trending")
            search_box.send_keys(Keys.RETURN)

            # Give the heavy YouTube results page a few seconds to start rendering
            time.sleep(3)
        except TimeoutException:
            search_box_found = False

        # We fail outside the try/except block to avoid Python exception chaining (stacktraces)
        if not search_box_found:
            pytest.fail(
                f"TEST FAILED: Could not find the YouTube search box using the selector: {search_selector}",
                pytrace=False
            )

        print("-" * 50)
        # 3. Extract Titles
        yt_title_selector = "a#video-title"
        videos_found = True

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, yt_title_selector))
            )
        except TimeoutException:
            videos_found = False

        if not videos_found:
            pytest.fail(
                "TEST FAILED: Could not find any video titles within 10 seconds. Layout may have changed.",
                pytrace=False
            )

        video_elements = driver.find_elements(By.CSS_SELECTOR, yt_title_selector)

        print(f"Found {len(video_elements)} video titles in search results:")
        #This is amended to remove chained stacktrace errors in the test results
        for index, element in enumerate(video_elements[:15], 1):
            title = element.get_attribute("textContent").strip()
            if title:
                print(f"{index}. {title}")

    finally:
        driver.quit()