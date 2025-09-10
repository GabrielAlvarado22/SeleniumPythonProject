import os
from selenium import webdriver

def get_driver():
    browser = os.getenv("BROWSER", "chrome").lower()  # default = chrome

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")
        return webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--private")
        return webdriver.Firefox(options=options)

    elif browser == "safari":
        # To enable Safari driver run: safaridriver --enable
        return webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser}")
