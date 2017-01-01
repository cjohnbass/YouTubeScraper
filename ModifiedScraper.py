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
        self.driver.get(self.start_url)


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()


if __name__ =="__main__":
    start_url = sys.argv[1]

    with YouTubeSubtitlesScraper(start_url) as scraper:
        sys.exit()
