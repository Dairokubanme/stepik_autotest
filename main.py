import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    cena = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), text_="100"))
    btn = browser.find_element(By.CSS_SELECTOR, "#book")
    btn.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    otvet = browser.find_element(By.ID, "answer")
    otvet.send_keys(y)
    btn2 = browser.find_element(By.ID, "solve")
    btn2.click()

finally:
        time.sleep(5)
        browser.quit()