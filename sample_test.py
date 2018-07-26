import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://www.amazon.com/")
    driver.find_element_by_name("field-keywords").send_keys("echo")
    driver.find_element_by_css_selector(".nav-search-submit > input:nth-child(2)").click()
    WebDriverWait(driver, 10).until(EC.title_is("Amazon.com: echo"))