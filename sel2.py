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

    loginTab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'login_menu_button')]")))
    loginTab.click()
    time.sleep(5)
    nothnaksBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='pushpad_deny_button'])[1]")))
    nothnaksBtn.click()

    emailfield = driver.find_element(By.XPATH, "//input[@name='btc_address']")
    emailfield.send_keys('fawadstar449672@gmail.com')
    passfield = driver.find_element(By.XPATH, "//input[@id='login_form_password']")
    passfield.send_keys('Jk,FVD8t5vUfdtM')

    loginBtn = driver.find_element(By.XPATH, "//button[@id='login_button']")
    loginBtn.click()
    time.sleep(20)
    checkBtn = driver.find_element(By.XPATH, "//div[@id='checkbox']")
    checkBtn.click()


finally:
    pass
