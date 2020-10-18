import pathlib
import json
from selenium import webdriver

driver = webdriver.Chrome('chrome86-driver.exe')
driver.get("https://amazon.com/")

input("Press enter once you are logged in: ")

with pathlib.Path('./cookies.json').open(mode='w') as file:
    json.dump(driver.get_cookies(), file, indent=4)
