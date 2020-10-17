import time
from selenium import webdriver
from dotenv import dotenv_values
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

dotenv_dict = dotenv_values()
PHONE_OR_EMAIL_ADDRESS, PASSWORD, ASIN = (dotenv_dict['email_or_phone'],
                                          dotenv_dict['password'],
                                          dotenv_dict['asin'])

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

amazon_signin_button = WebDriverWait(driver, 10) \
                       .until(EC.presence_of_element_located((By.ID, 'nav-link-accountList')))

amazon_signin_button.click()

info_form = WebDriverWait(driver, 10) \
            .until(EC.presence_of_element_located((By.NAME, 'signIn')))

email_or_phone = info_form.find_element_by_id('ap_email')
email_or_phone.send_keys(PHONE_OR_EMAIL_ADDRESS)

info_form.submit()

info_form = WebDriverWait(driver, 10) \
            .until(EC.presence_of_element_located((By.NAME, 'signIn')))

password = info_form.find_element_by_id('ap_password')
password.send_keys(PASSWORD)

info_form.submit()

time.sleep(2)

driver.quit()
