from __future__ import annotations

from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@dataclass(frozen=True)
class ParcelConfigPage:
    url: str

    PARCEL_SIZE_HEADER = (By.XPATH, "//h2[normalize-space()='Parcel Size']")
    RECIPIENT_HEADER = (By.XPATH, "//h2[normalize-space()='Recipient']")
    DELIVERY_OPTIONS_HEADER = (By.XPATH, "//h2[normalize-space()='Delivery options']")

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[normalize-space()='Add to shopping cart']")

    def open(self, driver):
        driver.get(self.url)
        return self

    def wait_page_loaded(self, driver) -> None:
        driver.wait.until(EC.visibility_of_element_located(self.PARCEL_SIZE_HEADER))
        driver.wait.until(EC.visibility_of_element_located(self.RECIPIENT_HEADER))
        driver.wait.until(EC.visibility_of_element_located(self.DELIVERY_OPTIONS_HEADER))

    def wait_add_to_cart_ready(self, driver) -> None:
        driver.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
