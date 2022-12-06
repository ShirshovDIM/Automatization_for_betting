def bet (streak, driver, last_dot, blueButton, redButton):

    if streak == 2:
        if last_dot.find_element_by_css_selector('g').get_attribute('fill') == "#EC2024":
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='50']").click()
            blueButton.click()
        else:
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='50']").click()
            redButton.click() 
    
    if streak == 3:
        if last_dot.find_element_by_css_selector('g').get_attribute('fill') == "#EC2024":
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='250']").click() 
            blueButton.click()   
        else:
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='250']").click() 
            redButton.click()
    
    if streak == 4:
        if last_dot.find_element_by_css_selector('g').get_attribute('fill') == "#EC2024":
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='500']").click() 
            blueButton.click()   
        else:
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='500']").click() 
            redButton.click()

    if streak == 5:
        if last_dot.find_element_by_css_selector('g').get_attribute('fill') == "#EC2024":
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='1000']").click() 
            blueButton.click()   
        else:
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='1000']").click() 
            redButton.click()

    if streak == 6:
        if last_dot.find_element_by_css_selector('g').get_attribute('fill') == "#EC2024":
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='1000']").click() 
            blueButton.click()   
        else:
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='1000']").click() 
            redButton.click()

    if streak >= 7:
        if last_dot.find_element_by_css_selector('g').get_attribute('fill') == "#EC2024":
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='5000']").click() 
            blueButton.click()   
        else:
            driver.find_element_by_css_selector("div.toggle-chip-3--3-QaW > span > div").click()
            driver.find_element_by_css_selector(".chip--1itRi.disabled--2GE8f.cover--do2Tb[data-value='5000']").click() 
            redButton.click()