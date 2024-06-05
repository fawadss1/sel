import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get('https://freebitco.in')

    loginbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'login_menu_button')]")))
    loginbtn.click()
    time.sleep(5)
    nothnaksBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='pushpad_deny_button'])[1]")))
    nothnaksBtn.click()

    emailfield = driver.find_element(By.XPATH, "//input[@name='btc_address']")
    emailfield.send_keys('fawad.khan@suvastutech.com')

finally:
    pass
