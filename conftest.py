import pytest, logging, sys, os
from datetime import *
from collections import namedtuple
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import consts
from colorlogger import *
is_jenkins = False


def pytest_addoption(parser):
    parser.addoption("--jenkins", action="store", default=False)


def pytest_generate_tests(metafunc):
    global is_jenkins
    option_value = metafunc.config.option.jenkins
    if option_value is not None:
        is_jenkins = option_value


# Can change driver or have multiple driver here if needed
@pytest.fixture(params=["chrome"], scope="function")
def driver_init(request):
    options = None
    if request.param == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        if is_jenkins:
            print("Run on Jenkins with Chrome headless.")
            options.add_argument('disable-infobars')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-gpu')
            options.add_argument("--headless")
        else:
            print("Run on local dev/debug with Chrome")
        options.add_argument('start-maximized')
        options.add_argument("window-size=1366,768")
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        driver.get(consts.URL_KANOPY_STAGING_HOME)
        driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        driver.close()


@pytest.fixture(scope="class")
def logger_init(request):
    # c_handler = logging.StreamHandler(sys.stderr)
    # c_handler.setLevel(logging.INFO)
    #
    # c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    # c_handler.setFormatter(c_format)
    #
    # logger.addHandler(c_handler)
    # request.cls.logger = logger

    logger = logging.getLogger(request.cls.__name__)
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)
    request.cls.logger = logger

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    extra = getattr(rep, "extra", [])
    if rep.when == 'call' and rep.failed:
        screenshot_dir = "testCases/failed_screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        pytest_html = item.config.pluginmanager.getplugin("html")
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        feature_request = item.funcargs['request']
        screen_shot_file = f'{screenshot_dir}/{now}.png'

        driver = feature_request.cls.driver
        driver.save_screenshot(screen_shot_file)
        extra.append(pytest_html.extras.image(screen_shot_file))
        xfail = hasattr(rep, "wasxfail")
        rep.extra = extra


@pytest.fixture(scope="class")
def credentials_init(request):
    credentials = {
        "email": "qa-robot@revinate.com",
        "password": "ah8un1tErop6kINSEsTecOgend468GArs123"
    }

    request.cls.credentials = namedtuple('Struct', credentials.keys())(*credentials.values())
