import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ar, ca, cs, da, de, en-gb, el,"
                          "es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-cn")


def chosen_language(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': f'{language}'})
    browser = webdriver.Chrome(options=options)
    return browser


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    print(f"\nstart chrome browser with {language} language for test..")
    browser = chosen_language(language)
    yield browser
    print("\nquit browser..")
    browser.quit()
