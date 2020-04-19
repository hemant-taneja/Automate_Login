from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys

#Accessing drivers and webpage
browser = webdriver.Firefox()
browser.get("https://github.com/login")

#Finding Fields
username = browser.find_element_by_name("login")
password = browser.find_element_by_name("password")
submit   = browser.find_element_by_name("commit")

#Taking CLI params
user = sys.argv[1]
user_pass = sys.argv[2]

#Entering the data
username.send_keys(user)
password.send_keys(user_pass)

#Clicking on the login button
submit.click()
