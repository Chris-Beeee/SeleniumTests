import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# Import the Page Object
from pages.giantbomb_home import GiantBombHomePage

def test_giantbomb_video_titles():
    # Initialize the driver
    driver = webdriver.Chrome()
    
    try:
        # 1. Initialize the Page Object
        home_page = GiantBombHomePage(driver)
        
        # 2. Interact with the page
        print("Navigating to Giant Bomb...")
        home_page.load()
        
        print("Checking for popups...")
        home_page.accept_cookies_if_present()
        home_page.close_ads_if_present()
        
        # 3. Get the Data
        try:
            titles = home_page.get_video_titles()
        except TimeoutException:
            pytest.fail("TEST FAILED: Could not find video titles. Selectors may have changed.", pytrace=False)
            
        # 4. Assert / Verify
        assert len(titles) > 0, "No video titles were found on the page!"
        
        print(f"\nFound {len(titles)} video titles on the homepage:")
        for index, title in enumerate(titles, 1):
            print(f"{index}. {title}")
            
    finally:
        # Always close the browser
        driver.quit()
