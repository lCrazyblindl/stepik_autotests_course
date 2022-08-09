from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element(By.ID, 'input_value').text)
    answer = math.log(abs(12 * math.sin(x)))
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

