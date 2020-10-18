import time
import pathlib
import json
from selenium import webdriver
from dotenv import dotenv_values
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://amazon.com/")

with open('cookies.json') as file:
    for cookie in json.load(file):
        driver.add_cookie(cookie)

driver.refresh()
