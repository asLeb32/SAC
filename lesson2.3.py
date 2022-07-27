from operator import contains
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import math




def calc(x):
    return str(math.log(abs(12*math.sin(x))))



chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/stepik_course/chromedriver/stable/chromedriver")


try: 
    link1 = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    browser.get(link1)
    
    message = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    number = browser.find_element(By.ID, "input_value").text
    result = calc(int(number))

    textbox = browser.find_element(By.ID, "answer")
    textbox.send_keys(result)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()