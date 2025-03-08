import undetected_chromedriver as uc
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HOME_URL = "https://www.runescape.com/community"
DEBUG = True


def get_driver():
    options = uc.ChromeOptions()
    options.headless = False
    return uc.Chrome(options=options)


def accept_cookie(driver):
    logger.info("Looking for 'Use necessary cookies only' button to click.")
    try:
        cookies_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline"))
        )
        logger.info("Clicking 'Use necessary cookies only' button.")
        cookies_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to accept cookies")
    else:
        logger.info("Successfully clicked 'Use necessary cookies only' button.")