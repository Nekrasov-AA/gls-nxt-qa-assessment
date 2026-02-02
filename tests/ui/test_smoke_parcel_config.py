import pytest

from tests.ui.pages.parcel_config_page import ParcelConfigPage


@pytest.mark.smoke
def test_parcel_configuration_page_loads(driver, base_url):
    page = ParcelConfigPage(url=base_url).open(driver)
    page.wait_page_loaded(driver)


@pytest.mark.smoke
def test_add_to_cart_is_clickable(driver, base_url):
    page = ParcelConfigPage(url=base_url).open(driver)
    page.wait_page_loaded(driver)
    page.wait_add_to_cart_ready(driver)
