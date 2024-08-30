from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
import time

# settings for how the tests will be executed
do_not_close_browser = False # if True, the browser will stay open after the tests are done, otherwise it will close
hide_window = True # if True, the browser will not be shown while the tests are executed

# ---------------------------- This section of code starts the browser and loads the website ----------------------------
chr_options = Options()

if do_not_close_browser:
    chr_options.add_experimental_option("detach", True)

if hide_window:
    chr_options.add_argument("--headless")

chr_options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=chr_options)
driver.get(os.path.join(os.path.dirname(os.getcwd()), "JITS-pizzeria", 'index.html'))
# -------------------------------------------------------------------------------------------------------------------------

def save_screenshot(save_path, res_name, id): # function for shortening the code for saving screenshots
    driver.save_screenshot(save_path + res_name + id  + datetime.utcnow().strftime('%Y-%m-%d %H.%M.%S.%f')[:-3] + ".png") 

def screenshot_res(width, height, res_name, save_path):

    driver.set_window_size(width, height) # set the window size to the desired resolution

    html = driver.find_element(By.TAG_NAME, 'html') # prepare for scroll

    scroll(html, "top") # scroll to top
    # save screenshot of the top of the page with the resolution in the filename
    save_screenshot(save_path, res_name, " top ")

    scroll(html, "bottom") # scroll to bottom
    # save screenshot of the bottom of the page with the resolution in the filename
    save_screenshot(save_path, res_name, " bottom ")

    bg_images = driver.find_elements(By.CLASS_NAME, "background") # collect all elements with the class "background" in a list
    for img in bg_images: # iterate over the background images and take a screenshot of each
        scroll(html, img) # scroll to the image
        save_screenshot(save_path, res_name, " img-" + img.get_attribute("id") + " ")

def scroll(element, target):
    if type(target) == str:
        if target == "top":
            element.send_keys(Keys.HOME) # scroll to top

        elif target == "bottom":
            element.send_keys(Keys.END) # scroll to bottom

        time.sleep(0.2) # sleep for .2 seconds so the browser has time to scroll before taking screenshot

    elif type(target) == webdriver.remote.webelement.WebElement: # if the target is an element, scroll to the element
        actions = ActionChains(driver)
        actions.move_to_element(target).perform()

def capture_screenshots(): # generates a screenshot of the start page in two resolutions

    if os.path.isdir("generatedScreenshots") != True: # create a folder for the screenshots if it doesn't exist
        os.mkdir("generatedScreenshots")

    sub_folder_name = datetime.utcnow().strftime('%Y-%m-%d-%H.%M.%S.%f')[:-3] # create a subfolder-name with the current time
    save_path = "generatedScreenshots/" + sub_folder_name + "/" # set the save path to the subfolder
    os.mkdir(save_path) # create the subfolder

    screenshot_res(1920, 1080, "1080p", save_path) # test for checking desktop 1080p resolution
    screenshot_res(2560, 1440, "1440p", save_path) # test for checking desktop 1440p resolution
    # tests for checking phone resolutions
    screenshot_res(375, 667, "iPhone-SE", save_path) # iPhone SE
    screenshot_res(414, 896, "iPhone-XR", save_path) # iPhone XR
    screenshot_res(390, 844, "iPhone-12-Pro", save_path) # iPhone 12 Pro
    screenshot_res(430, 932, "iPhone-14-Pro-Max", save_path) # iPhone 14 Pro Max
    screenshot_res(412, 915, "Pixel-7-Samsung-S20-Ultra", save_path) # Pixel 7 / Samsung Galaxy S20 Ultra
    screenshot_res(360, 740, "Samsung-Galaxy-S8+", save_path) # Samsung Galaxy S8+

capture_screenshots()