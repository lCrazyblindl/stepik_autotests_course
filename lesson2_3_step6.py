from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
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

