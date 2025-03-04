from selene import browser
import pytest


@pytest.fixture(scope = "function", autouse = True)
def operations_with_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1024
    browser.config.window_height = 1024
    yield
    browser.quit()