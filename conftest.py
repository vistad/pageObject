
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):   # reads the language param from the CLI
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")

@pytest.fixture(scope="function")   # starts the browser in the defined language.
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\nstart browser for test..\nlanguage:{user_language}")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print("\nquit browser...")
    yield browser
    browser.quit()


