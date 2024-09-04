from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime, timezone
import time

# settings for how the tests will be executed
do_not_close_browser = False # if True, the browser will stay open after the tests are done, otherwise it will close
hide_window = True # if True, the browser will not be shown while the tests are executed

# ---------------------------- This section of code starts the browser and loads the website ----------------------------
chr_options = Options()
# chr_options = webdriver.ChromeOptions()

if do_not_close_browser:
    chr_options.add_experimental_option("detach", True)

if hide_window:
    chr_options.add_argument("--headless")

chr_options.add_argument("--disable-search-engine-choice-screen")
# -------------------------------------------------------------------------------------------------------------------------

def get_current_date_and_time(): # function for getting the current date and time
    return datetime.now(timezone.utc).strftime('%Y-%m-%d-%H.%M.%S.%f')[:-3] # return the current date and time in a specific format

def save_screenshot(driver, save_path, res_name, id): # function for shortening the code for saving screenshots
    driver.save_screenshot(save_path + res_name + id + "UTC" + get_current_date_and_time() + ".png") 


def screenshot_res(driver, width, height, res_name, save_path):

    driver.set_window_size(width, height) # set the window size to the desired resolution

    html = driver.find_element(By.TAG_NAME, 'html') # prepare for scroll

    scroll(driver, html, "top") # scroll to top
    # save screenshot of the top of the page with the resolution in the filename
    save_screenshot(driver, save_path, res_name, " top ")

    scroll(driver, html, "bottom") # scroll to bottom
    # save screenshot of the bottom of the page with the resolution in the filename
    save_screenshot(driver, save_path, res_name, " bottom ")

    bg_images = driver.find_elements(By.CLASS_NAME, "background") # collect all elements with the class "background" in a list
    for img in bg_images: # iterate over the background images and take a screenshot of each
        scroll(driver, html, img) # scroll to the image
        save_screenshot(driver, save_path, res_name, " img-" + img.get_attribute("id") + " ")

def scroll(driver, element, target):
    if type(target) == str:
        if target == "top":
            element.send_keys(Keys.HOME) # scroll to top

        elif target == "bottom":
            element.send_keys(Keys.END) # scroll to bottom

        time.sleep(0.2) # sleep for .2 seconds so the browser has time to scroll before taking screenshot

    elif type(target) == webdriver.remote.webelement.WebElement: # if the target is an element, scroll to the element
        actions = ActionChains(driver)
        actions.move_to_element(target).perform()

def capture_desktop_screenshots(save_path): # generates a screenshot of the start page in two resolutions

    driver = webdriver.Chrome(options=chr_options) # start the browser with the options
    driver.get(os.path.join(os.path.dirname(os.getcwd()), "JITS-pizzeria", 'index.html')) # load the website

    screenshot_res(driver, 1920, 1080, "1080p", save_path) # test for checking desktop 1080p resolution
    screenshot_res(driver, 2560, 1440, "1440p", save_path) # test for checking desktop 1440p resolution

    driver.quit() # close the browser

def screenshot_mobile_res(res_name, save_path):

    mobile_emulation = { "deviceName": res_name } # set the device name to the desired resolution
    chr_options.add_experimental_option("mobileEmulation", mobile_emulation) # set the mobile emulation option to the desired resolution

    driver = webdriver.Chrome(options=chr_options) # start the browser with the options
    driver.get(os.path.join(os.path.dirname(os.getcwd()), "JITS-pizzeria", 'index.html')) # load the website

    html = driver.find_element(By.TAG_NAME, 'html') # prepare for scroll

    scroll(driver, html, "top") # scroll to top
    # save screenshot of the top of the page with the resolution in the filename
    save_screenshot(driver, save_path, res_name, " top ")

    scroll(driver, html, "bottom") # scroll to bottom
    # save screenshot of the bottom of the page with the resolution in the filename
    save_screenshot(driver, save_path, res_name, " bottom ")

    bg_images = driver.find_elements(By.CLASS_NAME, "background") # collect all elements with the class "background" in a list
    for img in bg_images: # iterate over the background images and take a screenshot of each
        scroll(driver, html, img) # scroll to the image
        save_screenshot(driver, save_path, res_name, " img-" + img.get_attribute("id") + " ")

    driver.quit() # close the browser
    

def capture_mobile_screenshots(save_path):

    mobile_resolutions = ['iPhone SE', 'iPhone XR', 'iPhone 12 Pro', 'iPhone 14 Pro Max', 'Pixel 7', 'Samsung Galaxy S8+']

    for res in mobile_resolutions:
        screenshot_mobile_res(res, save_path) # take a screenshot of the website with the mobile resolution

def capture_screenshots():
    if os.path.isdir("generatedScreenshots") != True: # create a folder for the screenshots if it doesn't exist
        os.mkdir("generatedScreenshots")

    sub_folder_name = "UTC"+get_current_date_and_time() # create a subfolder-name with the current time
    save_path = "generatedScreenshots/" + sub_folder_name + "/" # set the save path to the subfolder
    os.mkdir(save_path) # create the subfolder

    capture_desktop_screenshots(save_path)
    capture_mobile_screenshots(save_path)

capture_screenshots() # run the function to capture the screenshots