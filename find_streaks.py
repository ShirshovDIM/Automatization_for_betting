from bet import bet
import time

def find_streaks(games, driver):
    try:
        for game in games:

            streak = 0

            table_name = game.find_element_by_css_selector(
                'span.tableName--3PUPn')

            last_dot = game.find_element_by_css_selector(
                '.item--1TwGJ div.roadContainer--2ujMr svg svg[data-type="coordinates"]:last-child')

            x_coor = last_dot.get_attribute("x")
            y_coor = last_dot.get_attribute("y")

            if y_coor == "5":
                print("\n" + table_name.text)

                upper_dot = True

                while (upper_dot):
                    try:
                        game.find_element_by_css_selector (f'.item--1TwGJ div.roadContainer--2ujMr svg svg[data-type="coordinates"][x="{x_coor}"][y="{str(int(y_coor) - 1)}"]')
                        upper_dot = False
                    except:
                        upper_dot = True
                    
                    streak += 1

                    x_coor = str(int(x_coor) - 1)
                print(streak)
                print(last_dot.find_element_by_css_selector('g').get_attribute('fill'))

                # red  #EC2024
                # blue #2E83FF

                blueButton = game.find_element_by_css_selector('div.footerControls--3u5nU > div:nth-child(1) > div')

                redButton = game.find_element_by_css_selector('div.footerControls--3u5nU > div:nth-child(2) > div')

                bet(streak, driver, last_dot, blueButton, redButton)

        find_streaks()

    except:
        time.sleep(5)
        driver.find_element_by_css_selector('div.right--350jI > button').click()
        find_streaks(games, driver)