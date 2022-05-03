from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

browser = webdriver.Firefox()
browser.implicitly_wait(5)

# username and password from cmd args

username = str(sys.argv[1])
password = str(sys.argv[2])

browser.get('https://www.instagram.com/')

sleep(2)

username_input = browser.find_element(by=By.NAME, value="username")
password_input = browser.find_element(by=By.NAME, value="password")


username_input.send_keys(username)
password_input.send_keys(password)

login_button =  browser.find_element(By.XPATH, value='/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
login_button.click()
