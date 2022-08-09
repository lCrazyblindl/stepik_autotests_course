from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    name1.send_keys("Haha")
    name2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    name2.send_keys("Hahah")
    email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys("Haha@.com")
    file_button = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')  # добавляем к этому пути имя файла
    file_button.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

