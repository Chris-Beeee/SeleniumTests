import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# Import the Page Object
from pages.youtube_home import YouTubeHomePage

def test_youtube_trending_search():
    # Initialize the driver
    driver = webdriver.Chrome()
    
    try:
        # 1. Initialize the Page Object
        home_page = YouTubeHomePage(driver)
        
        # 2. Interact with the page
        print("Navigating to YouTube...")
        home_page.load()
        
        print("Checking for cookie banners...")
        home_page.accept_cookies_if_present()
        
        print("Searching for 'trending' to bypass the empty history screen...")
        try:
            home_page.search("trending")
        except TimeoutException:
            pytest.fail("TEST FAILED: Could not find the YouTube search box.", pytrace=False)
        
        # 3. Get the Data
        print("-" * 50)
        try:
            # We can pass the limit of how many videos we want to the page object
            titles = home_page.get_video_titles(limit=15)
        except TimeoutException:
            pytest.fail("TEST FAILED: Could not find any video titles within the search results.", pytrace=False)
            
        # 4. Assert / Verify
        assert len(titles) > 0, "No video titles were found in the search results!"
        
        print(f"Found {len(titles)} video titles in search results:")
        for index, title in enumerate(titles, 1):
            print(f"{index}. {title}")
            
    finally:
        # Always close the browser
        driver.quit()
