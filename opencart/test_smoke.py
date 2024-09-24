"""
This module contains tests for smoke testing OpenCart.
"""

import pytest


@pytest.mark.run(order=1)
def test_smoke(driver):
    driver.get("http://localhost:8080/")
    assert "Your Store" in driver.title, "The page title does not indicate that" \
    " we are on the Opencart homepage"
