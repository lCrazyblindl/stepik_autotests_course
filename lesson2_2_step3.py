from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1')
    num1_prop = int(num1.text)
    num2 = browser.find_element(By.ID, 'num2')
    num2_prop = int(num2.text)
    answer = num1_prop + num2_prop
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(answer))
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

