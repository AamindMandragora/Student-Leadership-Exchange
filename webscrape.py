import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://tkmenus.com/aladdin/imsa')
info = []
for x in range(6):
    time.sleep(1)
    calendarBtn = driver.find_elements(By.XPATH, "//button[@type='button']")
    calendarBtn[1].click()
    time.sleep(1)
    weeks = driver.find_elements(By.XPATH, "//a[@class='calendar-week']")
    print(len(weeks))
    weeks[min(x, 4)].click()
    time.sleep(1)
    winfo = []
    for y in range(7):
        days = driver.find_elements(By.CLASS_NAME, "slick-active")
        days[y+1].click()
        time.sleep(10)
        infoButtons = driver.find_elements(By.XPATH, "//div[@class='menu-item-button ntr-info']")
        dInfo = {}
        print("num of foods today: %s" % len(infoButtons))
        for ibtn in infoButtons:
            ibtn.click()
            time.sleep(0.3)
            name = driver.find_element(By.XPATH, "//span[@class='menu-item-name']")
            if name.text in ["CLOSED", "CHECK BACK LATER"]:
                driver.find_element(By.XPATH, "//button[@class='close pull-right fs40']").click()
                continue
            dInfo[name.text] = driver.find_element(By.XPATH, "//table[@class='table table-striped modal-dialog-table']")
            driver.find_element(By.XPATH, "//button[@class='close pull-right fs40']").click()
        winfo.append(dInfo)
    info.append(winfo)
for x in range(len(info)):
    for y in range(x):
        if info[x] == info[y]:
            print(x, y)