"""
Author: TH
Date: 07/06/2016
Idea comes from: http://stackoverflow.com/questions/28871115/scraping-infinite-scrolling-website-with-selenium-in-python
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys

import unittest, time, re
from collectTweets import collectTweets

class Sel(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stocktwits.com/symbol/AAPL?q=AAPL"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        #driver.find_element_by_link_text("All").click()
        for i in range(1,1000):
        #for i in range(1,3):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # the sententce to make website auto scrolling
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        with open('result.txt', 'wb') as f:
            f.write(data)
        collectTweets(data, 'AAPL')

if __name__ == "__main__":
    unittest.main()