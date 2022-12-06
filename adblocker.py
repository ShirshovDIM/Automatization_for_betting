from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

def adblocker(driver):
    try: #pop-up detect and close
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, ".new-popup__container")))
        driver.find_element_by_css_selector('button.new-popup__btn-close').click()
    except:
        print('No pop-up found')