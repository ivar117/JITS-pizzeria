from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime



class TestWebsite(TestCase):

    # settings for how the tests will be executed
    do_not_close_browser = False  # if True, the browser will stay open after the tests are done, otherwise it will close
    hide_window = True  # if True, the browser will not be shown while the tests are executed

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

    # tearDown is executed AFTER EVERY TEST
    def tearDown(self):
        self.browser.get('about:blank')  # load a blank page to avoid previous tests affecting subsequent tests

    # THE TESTS START HERE
    def testTitle(self):
        self.assertIn("Il Forno Magico", self.browser.page_source)

    def testTelephone(self):
        self.assertIn("0630-555-555", self.browser.page_source)

    def testOpeningHours(self):
        self.assertIn("Öppettider", self.browser.page_source)

    def testAddress(self):
        self.assertIn("Adress", self.browser.page_source)
    
    def testContact(self):
        self.assertIn("Kontakt", self.browser.page_source)

    def testCaptureScreenshot(self): # generates a screenshot of the start page
        self.browser.save_screenshot(datetime.utcnow().strftime('%Y-%m-%d %H.%M.%S.%f')[:-3] + ".png")

    def testContactLinks(self):
        contact_links = {
            "email": "mailto:info@ilfornomagico.se",
            "phone": "tel:0630-555-555",
        }

        for contact_type, expected_url in contact_links.items():
            link_element = self.browser.find_element(By.ID, contact_type)
            href = link_element.get_attribute('href')
            self.assertEqual(href, expected_url, f"{contact_type} link is incorrect.")

    def testSocialMediaLinks(self):
        social_links = {
            "facebook": "https://facebook.com/ntiuppsala",
            "instagram": "https://instagram.com/ntiuppsala",
            "twitter": "https://twitter.com/ntiuppsala"
        }

        for platform, expected_url in social_links.items():
            link_element = self.browser.find_element(By.ID, platform)
            link_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, platform))
            )
            href = link_element.get_attribute('href')
            
            # Test if the href matches the expected URL
            self.assertEqual(href, expected_url, f"{platform} link is incorrect.")

    def testCaptureScreenshot(self): # generates a screenshot of the start page in two resolutions

        os.path.isdir("testScreenshots") or os.mkdir("testScreenshots") # create a folder for the screenshots if it doesn't exist

        test_screenshot_res(self, 1920, 1080, "1080p")
        test_screenshot_res(self, 2560, 1440, "1440p")

        # tests for checking phone resolution
        test_screenshot_res(self, 375, 667, "iPhone-SE") # iPhone SE
        test_screenshot_res(self, 414, 896, "iPhone-XR") # iPhone XR
        test_screenshot_res(self, 390, 844, "iPhone-12-Pro") # iPhone 12 Pro
        test_screenshot_res(self, 430, 932, "iPhone-14-Pro-Max") # iPhone 14 Pro Max
        test_screenshot_res(self, 412, 915, "Pixel-7-Samsung-S20-Ultra") # Pixel 7 / Samsung Galaxy S20 Ultra
        test_screenshot_res(self, 360, 740, "Samsung-Galaxy-S8+") # Samsung Galaxy S8+
        
    def testBackgroundImage(self):
        bdy = self.browser.find_element(By.TAG_NAME, 'body') # stores "body"-element in variable

        bdy_bg_path = bdy.value_of_css_property("background-image").split("///")[1].split("\"")[0].replace("%20", " ") # finds the name of the "background-image"-property of "body"
        
        assert os.path.exists(bdy_bg_path) == True # check that background image of "body" exists

def test_screenshot_res(self, width, height, res_name):
    
    self.browser.set_window_size(width, height) # set the window size to the desired resolution

    # save screenshot with the resolution in the filename
    self.browser.save_screenshot("testScreenshots/" + res_name + " " + datetime.utcnow().strftime('%Y-%m-%d %H.%M.%S.%f')[:-3] + ".png")

# this code is here so that the tests will be executed if the file is executed as a normal python program
if __name__ == '__main__':
    main(verbosity=2)
