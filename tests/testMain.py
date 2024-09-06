from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import os
from datetime import datetime
import time


class TestWebsite(TestCase):

    # settings for how the tests will be executed
    do_not_close_browser = False # if True, the browser will stay open after the tests are done, otherwise it will close
    hide_window = True # if True, the browser will not be shown while the tests are executed

    # setUpClass is executed BEFORE THE FIRST test
    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.do_not_close_browser:
            chr_options.add_experimental_option("detach", True)

        if cls.hide_window:
            chr_options.add_argument("--headless")

        chr_options.add_argument("--disable-search-engine-choice-screen")
        cls.browser = webdriver.Chrome(options=chr_options)

    # tearDownClass is executed AFTER THE LAST test
    @classmethod
    def tearDownClass(cls):
        pass

    # setUp is executed BEFORE EVERY TEST
    def setUp(self):
        self.browser.get(os.path.join(os.path.dirname(os.getcwd()), "JITS-pizzeria", 'bootstrap.html'))

    # tearDown is executed AFTER EVERY TEST
    def tearDown(self):
        self.browser.get('about:blank')  # load a blank page to avoid previous tests affecting subsequent tests

    # THE TESTS START HERE
    def testWelcomeTitle(self):
        self.assertIn("Il Forno Magico", self.browser.page_source)

    def testWelcomeTelephone(self):
        welcome_center_element = self.browser.find_element(By.ID, "welcome-center") # find the element with the id of "welcome-center"
        self.assertIn("0630-555-555", welcome_center_element.text)

    def testOpeningHours(self):
        opening_hours_div = self.browser.find_element(By.ID, "opening-hours") # find the element with the class of "opening-hours"
        compare_string = "Öppettider\nMån-Tor\nFredag\nLördag\nSöndag\n10-22\n10-23\n12-23\n12-20"
        self.assertIn(compare_string, opening_hours_div.text)

    def testAddress(self):
        address_div = self.browser.find_element(By.ID, "address") # find the element with the class of "address"
        compare_string = "Adress\nFjällgatan 32H\n981 39 KIRUNA"
        self.assertIn(compare_string, address_div.text)
    
    def testContact(self):
        contact_div = self.browser.find_element(By.ID, "contact") # find the element with the class of "contact"
        compare_string = "Kontakt\n0630-555-555\ninfo@ilfornomagico.se"
        self.assertIn(compare_string, contact_div.text)

    def testContactLinks(self): 
        self.assertIn("mailto:info@ilfornomagico.se", self.browser.page_source)
        self.assertIn("tel:0630-555-555", self.browser.page_source)

    def testSocialMediaLinks(self): 
        self.assertIn("https://facebook.com/ntiuppsala", self.browser.page_source)
        self.assertIn("https://instagram.com/ntiuppsala", self.browser.page_source)
        self.assertIn("https://x.com/ntiuppsala", self.browser.page_source)
        
    def testImagesPath(self):
        images = self.browser.find_elements(By.TAG_NAME, 'img') # collect all img elements on the page in a list

        for img in images: # iterate over the images
            img_src_path = img.get_attribute("src") # get the path source of the image
            img_src_path = img_src_path[8:] # remove "file:///" from the path, which are the first 8 characters
            assert os.path.exists(img_src_path) # check that the source of the image exists

# this code is here so that the tests will be executed if the file is executed as a normal python program
if __name__ == '__main__':
    main(verbosity=2)
