from cgitb import reset
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))




chrome_options = Options()
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/stepik_course/chromedriver/stable/chromedriver")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "privet.txt"
file_path = os.path.join(current_dir, file_name)


try: 
    link1 = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    browser.get(link1)
    fields = ["firstname", "lastname", "email"]
    for name in fields:
        inform = browser.find_element(By.NAME, name)
        inform.send_keys("Sasha")
    file_input = browser.find_element(By.CSS_SELECTOR, "#file")
    file_input.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()