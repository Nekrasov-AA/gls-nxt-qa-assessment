import re
from pathlib import Path
from datetime import datetime, timezone

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


DEFAULT_BASE_URL = "https://www.gls-pakete.de/en/private-customers/parcel-shipping/parcel-configuration"


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--base-url", action="store", default=DEFAULT_BASE_URL)
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--wait-timeout", action="store", default="10")


@pytest.fixture(scope="session")
def base_url(request: pytest.FixtureRequest) -> str:
    return str(request.config.getoption("--base-url"))


@pytest.fixture(scope="session")
def wait_timeout(request: pytest.FixtureRequest) -> int:
    return int(request.config.getoption("--wait-timeout"))


@pytest.fixture()
def driver(request: pytest.FixtureRequest, wait_timeout: int):
    headless = bool(request.config.getoption("--headless"))

    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if headless:
        options.add_argument("--headless=new")
    service = ChromeService(ChromeDriverManager().install())

    _driver = webdriver.Chrome(service=service, options=options)
    _driver.set_page_load_timeout(30)

    _driver.wait = WebDriverWait(_driver, wait_timeout)

    yield _driver

    _driver.quit()


def _safe_filename(nodeid: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_.-]+", "_", nodeid)
    return cleaned[:180]


# Attach UI debug artifacts (screenshot + HTML) when test fails.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or report.passed:
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    name = _safe_filename(item.nodeid)

    screenshot_path = artifacts_dir / f"{name}_{ts}.png"
    html_path = artifacts_dir / f"{name}_{ts}.html"

    try:
        driver.save_screenshot(str(screenshot_path))
    except Exception:
        pass

    try:
        html_path.write_text(driver.page_source, encoding="utf-8")
    except Exception:
        pass

    report.sections.append(("artifacts", f"screenshot: {screenshot_path}\nhtml: {html_path}\n"))
