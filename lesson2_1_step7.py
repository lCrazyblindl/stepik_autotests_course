from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    image = browser.find_element(By.CSS_SELECTOR, 'img[src="images/chest.png"]')
    x = image.get_attribute('valuex')
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)
    robot = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robot.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

