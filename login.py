import pyotp
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from main import accept_cookie


def navigate_to_login_page(driver):
    logger.info("Looking for 'Account' button to click.")
    try:
        account_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='home']/div/header/div[2]/div/nav/a[3]"))
        )
        logger.info("Clicking 'Account' button.")
        account_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to navigate to login page")
        driver.close()
    else:
        logger.info("Successfully clicked 'Account' button.")


def enter_email(driver, email):
    logger.info(f"Entering email address ({email}) into the email input field.")
    try:
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='email']")))
        email_field = driver.switch_to.active_element
        email_field.send_keys(email)
    except Exception:
        logger.error(f"An error occurred while trying to fill the email input field.")
        driver.close()
    else:
        logger.info("Successfully filled the 'email input field'.")


def click_submit_button(driver):
    logger.info("Looking for 'submit' button to click.")
    try:
        submit_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='continue-with-assisted-via-email-flow']"))
        )
        logger.info("Clicking 'submit' button.")
        submit_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to click the submit button")
        driver.close()
    else:
        logger.info("Successfully clicked 'submit' button.")


def enter_password(driver, password):
    logger.info(f"Entering password ({password}) into the password input field.")
    try:
        password_field = (WebDriverWait(driver, 40).until
                          (EC.visibility_of_element_located((By.XPATH, "//*[@id='login-password']"))))
        password_field.send_keys(password)
    except Exception:
        logger.error(f"An error occurred while trying to fill the password input field.")
        driver.close()
    else:
        logger.info("Successfully filled the 'password input field'.")


def click_login_button(driver):
    logger.info("Looking for 'login' button to click.")
    try:
        login_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='du-login-submit']"))
        )
        logger.info("Clicking 'login' button.")
        login_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to click the login button")
        driver.close()
    else:
        logger.info("Successfully clicked 'login' button.")


def enter_authenticator(driver, authenticator):
    logger.info("Looking for 'authenticator input field' to fill.")
    try:
        authenticator_field = (WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/main/div/div/form/label[1]/input"))))
        totp = pyotp.TOTP(authenticator)

        authenticator_field.send_keys(totp.now())
    except Exception:
        logger.error(f"An error occurred while trying to fill the authenticator input field.")
        driver.close()
    else:
        logger.info("Successfully filled the 'authenticator input field'.")


def click_2fa_submit_button(driver):
    logger.info("Looking for '2fa submit' button to click.")
    try:
        submit_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button"))
        )
        logger.info("Clicking '2fa submit' button.")
        submit_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to click the 2fa submit button")
        driver.close()
    else:
        logger.info("Successfully clicked '2fa submit' button.")


def login(driver, EMAIL, PASSWORD, AUTHENTICATOR):
    accept_cookie(driver)
    navigate_to_login_page(driver)
    accept_cookie(driver)

    enter_email(driver, EMAIL)
    accept_cookie(driver)

    click_submit_button(driver)
    accept_cookie(driver)

    enter_password(driver, PASSWORD)
    click_login_button(driver)

    if AUTHENTICATOR is not None:
        enter_authenticator(driver, AUTHENTICATOR)
        click_2fa_submit_button(driver)
