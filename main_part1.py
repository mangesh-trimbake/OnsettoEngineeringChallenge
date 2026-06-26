from config import *

from utils.driver import get_driver

from pages.login_page import LoginPage
from pages.account_page import AccountPage


def main():

    driver = get_driver()

    try:

        login = LoginPage(driver)

        login.login(
            EMAIL,
            PASSWORD
        )

        login.verify_mfa(
            MFA_CODE
        )

        account = AccountPage(driver)

        account.open_account()

        account.update_banking(
            BANK_ROUTING,
            BANK_ACCOUNT
        )

        account.update_payment(
            CARD_HOLDER,
            CARD_NUMBER,
            CARD_MONTH,
            CARD_YEAR,
            CARD_CVC
        )

        account.verify()

        driver.save_screenshot("success.png")

        print("\nAutomation Completed Successfully.")

    except Exception as e:

        print(e)

        driver.save_screenshot("error.png")

    finally:

        input("\nPress Enter to close browser...")

        driver.quit()


if __name__ == "__main__":
    main()