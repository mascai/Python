from selenium import webdriver
import requests
from itertools import cycle
import traceback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.wikipedia.org/")

elem = driver.find_element_by_tag_name("html")
elem.send_keys(Keys.END)
time.sleep(6)
elem.send_keys(Keys.HOME)
