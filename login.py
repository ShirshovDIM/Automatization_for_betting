from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
import credentials


def authenticate(driver):

    WebDriverWait(driver, 200).until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, ".btn.btn_outline.btn_medium")))
    driver.find_element_by_css_selector(
        '.btn.btn_outline.btn_medium').click()

    WebDriverWait(driver, 200).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, ".input__value")))
    loginInput = driver.find_elements_by_css_selector('.input__value')[0]
    loginInput.clear()
    loginInput.send_keys(credentials.login)
    time.sleep(2)

    passInput = driver.find_elements_by_css_selector('.input__value')[1]
    passInput.clear()
    passInput.send_keys(credentials.password)

    submit_button = driver.find_element_by_css_selector(
        '.btn.btn_large.btn_block.btn_red')
    submit_button.click()