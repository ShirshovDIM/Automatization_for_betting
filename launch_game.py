from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

def launch_games(driver):
    # Set TRX currency
    WebDriverWait(driver, 200).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, ".balance__inner")))

    driver.find_element_by_css_selector('.balance__inner').click()
    driver.find_element_by_css_selector(
        'div.balance-dropdown__inner.balance-dropdown__inner--darkened > ul > li:nth-child(4)').click()

    # Start game
    WebDriverWait(driver, 200).until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, "#play_button")))
    driver.find_element_by_css_selector('#play_button').click()

    # Switch to game iframe
    WebDriverWait(driver, 200).until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, "div.single-game-modal-body-block iframe")))
    driver.switch_to.frame(driver.find_element_by_css_selector(
        "div.single-game-modal-body-block iframe"))

    WebDriverWait(driver, 200).until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, "div.multiplayButtonContainer--a_4PI > div > div > button")))
    driver.find_element_by_css_selector(
        "div.multiplayButtonContainer--a_4PI > div > div > button").click()

    # Switch to game side-bar iframe
    WebDriverWait(driver, 200).until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, "div.sidebar-container > iframe")))
    driver.switch_to.frame(driver.find_element_by_css_selector(
        "div.sidebar-container > iframe"))

    # Collect games
    WebDriverWait(driver, 200).until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, ".item--1TwGJ")))
    games = driver.find_elements_by_css_selector(".item--1TwGJ")

    WebDriverWait(driver, 200).until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, "svg > svg > g")))
    
    return(games)