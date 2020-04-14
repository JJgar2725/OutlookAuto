import sys
import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome()
driver.get("https://my.utrgv.edu/web/myutrgv/home")

username = driver.find_element_by_id("_58_username")
username.send_keys(os.environ['USER-NAME'])

password = driver.find_element_by_id("_58_password")
password.send_keys(os.environ['PASSWORD'])

submit_button = driver.find_element_by_xpath('//*[@id="_58_fm"]/div/button').click()

driver.implicitly_wait(10)  # FIXME: USE EXPLICIT WAITING
outlook_select = driver.find_element_by_xpath('//*[@id="portlet_utrgvgraphemailportlet_WAR_utrgvgraphemailportlet"]/div/div/div/div/article[1]/a').click()

driver.implicitly_wait(20)  # FIXME: USE EXPLICIT WAITING
new_message = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/button').click()
