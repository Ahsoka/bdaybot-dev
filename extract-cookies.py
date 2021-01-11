import pathlib
import json
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time

load_dotenv()

email = os.environ["email"]
password = os.environ["password"]


if os.name == 'posix':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless'); # chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=str(pathlib.Path('chrome86-driver').resolve()),
                                      chrome_options=chrome_options,
                                      service_args=['--verbose', f"--log-path={pathlib.Path('logs/chrome.log').resolve()}"])
    driver.set_window_size(width=1363, height=1094)
else:
    driver = webdriver.Chrome('chrome86-driver.exe')

driver.get("https://amazon.com/")

amazon_signin_button = WebDriverWait(driver, 10) \
                       .until(EC.presence_of_element_located((By.ID, 'nav-link-accountList')))

amazon_signin_button.click()

info_form = WebDriverWait(driver, 10) \
            .until(EC.presence_of_element_located((By.NAME, 'signIn')))

email_or_phone = info_form.find_element_by_id('ap_email')
email_or_phone.send_keys(email)

info_form.submit()

info_form = WebDriverWait(driver, 10) \
            .until(EC.presence_of_element_located((By.NAME, 'signIn')))

passwordbtn = info_form.find_element_by_id('ap_password')
passwordbtn.send_keys(password)

info_form.submit()

time.sleep(2)

driver.save_screenshot(str(pathlib.Path("screenshot.png").resolve()))


with pathlib.Path('./cookies.json').open(mode='w') as file:
    json.dump(driver.get_cookies(), file, indent=4)
