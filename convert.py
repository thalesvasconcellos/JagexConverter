import time

from loguru import logger
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import main
from commons.utils.utility import is_valid_email, generate_random_password
from login import login
from main import accept_cookie


def click_upgrade_button(driver):
    logger.info("Looking for 'upgrade' button to click.")
    try:
        upgrade_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='p-settings']/div/section[1]/a"))
        )
        logger.info("Clicking 'upgrade' button.")
        upgrade_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to click the upgrade button")
        driver.close()
    else:
        logger.info("Successfully clicked 'upgrade' button.")


def click_upgrade_submit_button(driver):
    logger.info("Looking for 'upgrade submit' button to click.")
    try:
        submit_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div/div/div/button"))
        )
        logger.info("Clicking 'upgrade submit' button.")
        submit_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to click the upgrade submit button")
        driver.close()
    else:
        logger.info("Successfully clicked 'upgrade submit' button.")


def enter_upgrade_email(driver, email):
    logger.info(f"Entering email address ({email}) into the email input field.")
    try:
        (WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='email']"))))
        authenticator_field = driver.switch_to.active_element
        authenticator_field.send_keys(email)
    except Exception:
        logger.error(f"An error occurred while trying to fill the email input field.")
        driver.close()
    else:
        logger.info("Successfully filled the 'email input field'.")


def enter_upgrade_dob(driver):
    logger.info(f"Entering 'date of birth' into the respective fields.")
    try:
        action = ActionChains(driver)

        day_field = (WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/form/div[4]/div[1]/div/label/input"))))
        action.move_to_element(day_field).perform()
        day_field.send_keys("2")

        month_field = (WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/form/div[4]/div[2]/div/label/input"))))
        action.move_to_element(month_field).perform()
        month_field.send_keys("10")

        year_field = (WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/form/div[4]/div[3]/div/label/input"))))
        action.move_to_element(year_field).perform()
        year_field.send_keys("2000")
    except Exception:
        logger.error(f"An error occurred while trying to enter 'date of "
                     f"birth' into the respective fields.")
        driver.close()
    else:
        logger.info("Successfully entered 'date of birth' into the respective fields.")


def click_agree_checkbox(driver):
    logger.info("Looking for 'I agree' checkbox to click.")
    try:
        submit_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='registration-start-accept-agreements']"))
        )
        logger.info("Clicking 'I agree' checkbox.")
        submit_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to click the 'I agree' checkbox")
        driver.close()
    else:
        logger.info("Successfully clicked 'I agree' checkbox.")


def click_continue_button(driver):
    logger.info("Looking for 'continue' button to click.")
    try:
        continue_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/form/button"))
        )
        logger.info("Clicking 'continue' button.")
        continue_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to click the 'continue' button")
        driver.close()
    else:
        logger.info("Successfully clicked 'continue' button.")


def access_email_on_website(driver, username):
    logger.info("Looking for access email on new tab.")
    try:
        new_tab_url = f"https://tuamaeaquelaursa.com/{username}"
        driver.execute_script(f"window.open('{new_tab_url}', '_blank');")

        driver.switch_to.window(driver.window_handles[1])
    except Exception:
        logger.error(f"An error occurred while trying to access email on new tab")
        driver.close()
    else:
        logger.info("Successfully accessed email on new tab.")


def get_verification_code(driver):
    logger.info("Looking for verification code.")
    try:
        div_element = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/div"))
        )

        first_element = div_element.find_element(By.XPATH, ".//*")
        subject = first_element.find_element(By.CLASS_NAME, "the-message-subject")

        verification_code = subject.text.split(" ")[0]
        logger.info(f"Successfully gather verification code ({verification_code}).")

        return verification_code
    except Exception:
        logger.error(f"An error occurred while trying to get verification code")
        driver.close()


def enter_verification_code(driver, code):
    logger.info(f"Entering verification code ({code}) into the verification code input field.")
    try:
        driver.switch_to.window(driver.window_handles[0])

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/form/div[1]/label/input"))
        )

        verification_code = driver.switch_to.active_element
        verification_code.send_keys(code)
    except Exception:
        logger.error(f"An error occurred while trying to fill the verification code input field.")
        driver.close()
    else:
        logger.info("Successfully filled the verification code input field.")


def enter_username(driver, username):
    logger.info(f"Entering username ({username}) into the username input field.")
    try:
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

        username_field = (WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/form/div[1]/label/input"))))
        username_field.send_keys(username)
    except Exception:
        logger.error(f"An error occurred while trying to fill the username input field.")
        driver.close()
    else:
        logger.info("Successfully filled the username input field.")


def enter_jagex_password(driver, password):
    logger.info(f"Entering password ({password}) into the password input field.")
    try:
        password_field = (WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/form/div[1]/label/input"))))
        password_field.send_keys(password)

        time.sleep(1)

        repassword_field = (WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/form/div[3]/label/input"))))
        repassword_field.send_keys(password)
    except Exception:
        logger.error(f"An error occurred while trying to fill the password input field.")
        driver.close()
    else:
        logger.info("Successfully filled the password input field.")


def click_confirm_creation(driver):
    logger.info("Looking for 'continue' button to click.")
    try:
        continue_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/a"))
        )
        logger.info("Clicking 'continue' button.")
        continue_button.click()
    except Exception:
        logger.error(f"An error occurred while trying to click the 'continue' button.")
        driver.close()
    else:
        logger.info("Successfully clicked 'continue' button.")


def convert(driver, EMAIL, PASSWORD, AUTHENTICATOR, BASE_USERNAME, JAGEX_ACCOUNT_EMAIL, JAGEX_ACCOUNT_PASSWORD):
    login(driver, EMAIL, PASSWORD, AUTHENTICATOR)

    click_upgrade_button(driver)
    accept_cookie(driver)

    click_upgrade_submit_button(driver)
    enter_upgrade_email(driver, JAGEX_ACCOUNT_EMAIL)
    enter_upgrade_dob(driver)
    click_agree_checkbox(driver)
    click_continue_button(driver)

    access_email_on_website(driver, BASE_USERNAME)
    time.sleep(10)

    code = get_verification_code(driver)
    enter_verification_code(driver, code)
    click_continue_button(driver)
    time.sleep(10)

    enter_username(driver, BASE_USERNAME)
    click_continue_button(driver)
    time.sleep(1)

    enter_jagex_password(driver, JAGEX_ACCOUNT_PASSWORD)
    click_continue_button(driver)
    click_confirm_creation(driver)

    with open('accounts_generated.txt', 'a') as file:
        file.write(f"{JAGEX_ACCOUNT_EMAIL}:{JAGEX_ACCOUNT_PASSWORD}\n")

    time.sleep(20)

    first_window = driver.window_handles[0]
    for window in driver.window_handles[1:]:
        driver.switch_to.window(window)
        driver.close()

    driver.switch_to.window(first_window)
    driver.close()


if __name__ == '__main__':
    if not main.DEBUG:
        logger.remove()

    with open('accounts.txt', 'r') as file:
        lines = [line.strip() for line in file]

    for line in lines:
        COMBO_SPLIT = line.split(":")
        EMAIL, PASSWORD, AUTHENTICATOR = COMBO_SPLIT[0], COMBO_SPLIT[1], COMBO_SPLIT[2] if len(
            COMBO_SPLIT) >= 3 else None

        if not is_valid_email(EMAIL):
            logger.error(f"The account ({line.split()[0]}) doesn't have a email login.")
            continue

        BASE_USERNAME = EMAIL.split("@")[0].split(".")[0][0:8]

        JAGEX_ACCOUNT_EMAIL = BASE_USERNAME + "@tuamaeaquelaursa.com"
        JAGEX_ACCOUNT_PASSWORD = generate_random_password()

        driver = main.get_driver()
        driver.set_window_size(1024, 768)

        driver.get(main.HOME_URL)

        try:
            convert(driver, EMAIL, PASSWORD, AUTHENTICATOR, BASE_USERNAME, JAGEX_ACCOUNT_EMAIL, JAGEX_ACCOUNT_PASSWORD)
        except Exception:
            print(f"\033[31mThe account with email({EMAIL}) conversion could not be completed.\033[0m")
            continue
        else:
            print(f"\033[32mAccount with email ({JAGEX_ACCOUNT_EMAIL}) and password "
                  f"({JAGEX_ACCOUNT_PASSWORD}) has been converted.\033[0m")
