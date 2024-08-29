from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from http import * # import the http module to be able to use the http.server class
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
        self.browser.get(os.path.join(os.path.dirname(os.getcwd()), "JITS-pizzeria", 'index.html'))
        # self.browser.get("http://localhost:5500") # load the website

    # tearDown is executed AFTER EVERY TEST
    def tearDown(self):
        self.browser.get('about:blank')  # load a blank page to avoid previous tests affecting subsequent tests

    # THE TESTS START HERE
    def testTitle(self):
        self.assertIn("Il Forno Magico", self.browser.page_source)

    def testTelephone(self):
        welcome_center_element = self.browser.find_element(By.CLASS_NAME, "welcome-center") # find the element with the id of "contact_type"
        welcome_center_text = welcome_center_element.text # get the text of the element
        self.assertIn("0630-555-555", welcome_center_text)

    def testOpeningHours(self):
        self.assertIn("Öppettider", self.browser.page_source)

    def testAddress(self):
        self.assertIn("Adress", self.browser.page_source)
    
    def testContact(self):
        self.assertIn("Kontakt", self.browser.page_source)

    def testContactLinks(self): 
        self.assertIn("mailto:info@ilfornomagico.se", self.browser.page_source)
        self.assertIn("tel:0630-555-555", self.browser.page_source)

    def testSocialMediaLinks(self): 
        self.assertIn("https://facebook.com/ntiuppsala", self.browser.page_source)
        self.assertIn("https://instagram.com/ntiuppsala", self.browser.page_source)
        self.assertIn("https://twitter.com/ntiuppsala", self.browser.page_source)

    def testCaptureScreenshot(self): # generates a screenshot of the start page in two resolutions

        if os.path.isdir("testScreenshots") != True: # create a folder for the screenshots if it doesn't exist
            os.mkdir("testScreenshots")
        # os.path.isdir("testScreenshots") or os.mkdir("testScreenshots")

        test_screenshot_res(self, 1920, 1080, "1080p")
        test_screenshot_res(self, 2560, 1440, "1440p")

        # tests for checking phone resolution
        test_screenshot_res(self, 375, 667, "iPhone-SE") # iPhone SE
        test_screenshot_res(self, 414, 896, "iPhone-XR") # iPhone XR
        test_screenshot_res(self, 390, 844, "iPhone-12-Pro") # iPhone 12 Pro
        test_screenshot_res(self, 430, 932, "iPhone-14-Pro-Max") # iPhone 14 Pro Max
        test_screenshot_res(self, 412, 915, "Pixel-7-Samsung-S20-Ultra") # Pixel 7 / Samsung Galaxy S20 Ultra
        test_screenshot_res(self, 360, 740, "Samsung-Galaxy-S8+") # Samsung Galaxy S8+
        
    def testImagesPath(self):
        images = self.browser.find_elements(By.TAG_NAME, 'img') # collect all img elements on the page in a list

        for img in images: # iterate over the images
            img_src_path = img.get_attribute("src") # get the path source of the image
            img_src_path = img_src_path[8:] # remove "file:///" from the path, which are the first 8 characters
            assert os.path.exists(img_src_path) # check that the source of the image exists

def test_screenshot_res(self, width, height, res_name):
    
    self.browser.set_window_size(width, height) # set the window size to the desired resolution
    print(width, height)
    html = self.browser.find_element(By.TAG_NAME, 'html') # prepare for scroll

    scroll(self, html, "top") # scroll to top

    # save screenshot of the top of the page with the resolution in the filename
    self.browser.save_screenshot("testScreenshots/" + res_name + " top " + datetime.utcnow().strftime('%Y-%m-%d %H.%M.%S.%f')[:-3] + ".png")

    scroll(self, html, "bottom") # scroll to bottom

    # save screenshot of the bottom of the page with the resolution in the filename
    self.browser.save_screenshot("testScreenshots/" + res_name + " bottom " + datetime.utcnow().strftime('%Y-%m-%d %H.%M.%S.%f')[:-3] + ".png")

    bg_images = self.browser.find_elements(By.CLASS_NAME, "background") # collect all elements with the class "background" in a list

    for img in bg_images: # iterate over the background images and take a screenshot of each
        scroll(self, html, img)

        print("scrolling with res", res_name)

        self.browser.save_screenshot("testScreenshots/" + res_name + " img " + datetime.utcnow().strftime('%Y-%m-%d %H.%M.%S.%f')[:-3] + ".png")

def scroll(self, element, target):
    if type(target) == str:
        if target == "top":
            element.send_keys(Keys.HOME) # scroll to top

        elif target == "bottom":
            element.send_keys(Keys.END) # scroll to bottom

        time.sleep(0.2) # sleep for .2 seconds so the browser has time to scroll before taking screenshot

    elif type(target) == webdriver.remote.webelement.WebElement: # if the target is an element, scroll to the element
        actions = ActionChains(self.browser)
        actions.move_to_element(target).perform()

# this code is here so that the tests will be executed if the file is executed as a normal python program
if __name__ == '__main__':
    main(verbosity=2)
