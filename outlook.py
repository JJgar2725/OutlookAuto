# imported modules
import sys
import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# loads in dotenv variables
load_dotenv()

# creates a new Chrome window and maximizes
driver = webdriver.Chrome()
driver.maximize_window()

# creates system variables for later usage
email = str(sys.argv[1])
subject = str(sys.argv[2])

# goes to my.utrgv.edu
driver.get("https://my.utrgv.edu/web/myutrgv/home")

# finds text input and inputs username
username = driver.find_element_by_id("_58_username")
username.send_keys(os.environ['USER-NAME'])

# finds text input and inputs password
password = driver.find_element_by_id("_58_password")
password.send_keys(os.environ['PASSWORD'])

# finds submit button and hits it
submit_button = driver.find_element_by_xpath(
    '//*[@id="_58_fm"]/div/button').click()

# explicitly waits for page to load in and opens outlook
wait = WebDriverWait(driver, 10)
outlook_select = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="portlet_utrgvgraphemailportlet_WAR_utrgvgraphemailportlet"]/div/div/div/div/article[1]/a'))).click()

# explicitly waits for new window
waitAgain = WebDriverWait(driver, 10)

# gets a list of windows currently open
handles = driver.window_handles

# verifies that second window is open and waits for load-in
driver.switch_to.window(handles[1])
driver.implicitly_wait(10)

# finds New Message button, goes to it, and clicks it
driver.find_element(By.ID, "id__3").click()
element = driver.find_element(By.ID, "id__3")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

# user-defined info
driver.implicitly_wait(10)
actions = ActionChains(driver)
actions.send_keys(email)
actions.perform()

# necessary tabs
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()

actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()

actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()

actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()

# send subject
actions = ActionChains(driver)
actions.send_keys(subject)
actions.perform()

driver.implicitly_wait(2)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()

# send main message template
actions = ActionChains(driver)
actions.send_keys('Hello.\n\n\n\nThank you.\n\nJaime Garcia, Jr.')
actions.perform()

# done message
sys.exit('Done!')
