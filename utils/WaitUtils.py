from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visibility(self, by_locator):
        """Waits until the element is visible and returns it."""
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def wait_for_clickable(self, by_locator):
        """Waits until the element is clickable and returns it."""
        return self.wait.until(EC.element_to_be_clickable(by_locator))

    def wait_for_presence(self, by_locator):
        """Waits until the element is present in the DOM and returns it."""
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def wait_for_invisibility(self, by_locator):
        """Waits until the element is invisible."""
        return self.wait.until(EC.invisibility_of_element_located(by_locator))

    def wait_for_text(self, by_locator, text):
        """Waits until the element contains the specified text."""
        return self.wait.until(EC.text_to_be_present_in_element(by_locator, text))

    def wait_for_elements_present(self, by_locator, timeout=5):
        """
        Wait until at least one element is present in the DOM.
        Return a list of elements or an empty list if timeout occurs.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(lambda d: d.find_elements(*by_locator))
        except TimeoutException:
            return []  # Return empty list if no elements are found within timeout
