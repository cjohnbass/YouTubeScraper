import sys
import time
import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class YouTubeSubtitlesScraper():
  
    def __init__(self,start_url):
        self.start_url = start_url

    def __enter__(self):
        self.driver = webdriver.Chrome('C:\Program Files\ChromeDriver\chromedriver.exe')

        self.wait = WebDriverWait(self.driver, 10)

        self.driver.get(self.start_url)
        self.display_all_videos()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    def display_all_videos(self):
        """Click on "Load More" button to display all users videos."""
        while True:
            try:
                element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "yt-uix-load-more")))
                element.click()
            except TimeoutException:
                break

    def subtitles(self):
        """Visits video's page, enables 'CC' to scrape the subtitles and generates filename, link and the subtitles content."""
        videos = [(video.text, video.get_attribute("href"))
                  for video in self.driver.find_elements_by_class_name("yt-uix-tile-link")]
        
        for filename, link in videos:
            #self.driver.get(link)
           # self.enable_subtitles()

            #link = self.get_subtitles_link()
            yield filename, link, "blah"

if __name__ =="__main__":
    start_url = sys.argv[1]

    with YouTubeSubtitlesScraper(start_url) as scraper:
        print(type(scraper))
        for filename, link, content in scraper.subtitles():
            print(filename, link,content)