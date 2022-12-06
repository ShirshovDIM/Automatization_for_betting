from selenium import webdriver
from fake_useragent import UserAgent
import time

from adblocker import adblocker
from login import authenticate
from find_streaks import find_streaks
from launch_game import launch_games

ua = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={ua.chrome}")
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")

# disable webdriver-mode
options.add_argument("--disable-blink-features=AutomationControlled")

def main():

    try:
        # initiate webdriver
        driver = webdriver.Chrome(
            'chromeDriver/chromedriver.exe',
            options=options
        )

        driver.get('restricted_link')

        time.sleep(5)

        adblocker(driver)

        authenticate(driver)

        games = launch_games(driver)
        
        time.sleep(3)

        find_streaks(games, driver)

        time.sleep(10)
        driver.close()

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
