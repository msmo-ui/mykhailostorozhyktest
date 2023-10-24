import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Launching the Edge browser.............")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching the Firefox browser.............")
    else:
        driver = webdriver.Chrome()
        print("Launching the Chrome browser.............")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########################################  PyTest HTML Report  ########################################

def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Insider"
    config.stash[metadata_key]["Module Name"] = "Home & Careers"
    config.stash[metadata_key]["AQA"] = "Mykhailo Storozhyk"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
