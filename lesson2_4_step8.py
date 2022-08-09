from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()
    x = int(browser.find_element(By.ID, 'input_value').text)
    answer = math.log(abs(12*math.sin(x)))
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)
    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

