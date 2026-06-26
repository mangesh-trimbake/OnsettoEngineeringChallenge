from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage:

    def __init__(self,driver):

        self.driver = driver
        self.wait = WebDriverWait(driver,20)

    def open_account(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[@href='/app/account']"
                )
            )
        ).click()

        self.wait.until(
            EC.url_contains("/app/account")
        )

    def update_banking(self,routing,account):

        routing_box = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "bank-routing"
                )
            )
        )

        routing_box.clear()
        routing_box.send_keys(routing)

        account_box = self.driver.find_element(
            By.ID,
            "bank-account"
        )

        account_box.clear()
        account_box.send_keys(account)

        self.driver.find_element(
            By.ID,
            "bank-save"
        ).click()

    def update_payment(self,name,number,month,year,cvc):

        holder = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "card-holder"
                )
            )
        )

        holder.clear()
        holder.send_keys(name)

        self.driver.find_element(
            By.ID,
            "card-number"
        ).send_keys(number)

        self.driver.find_element(
            By.ID,
            "card-exp-month"
        ).send_keys(month)

        self.driver.find_element(
            By.ID,
            "card-exp-year"
        ).send_keys(year)

        self.driver.find_element(
            By.ID,
            "card-cvc"
        ).send_keys(cvc)

        self.driver.find_element(
            By.ID,
            "card-save"
        ).click()

    def verify(self):

        bank = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "[data-testid='bank-saved-info']"
                )
            )
        )

        payment = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "[data-testid='payment-saved-info']"
                )
            )
        )

        print("\nBank Summary")
        print(bank.text)

        print("\nPayment Summary")
        print(payment.text)

        assert "6789" in bank.text

        assert "4242" in payment.text

        print("\nVerification Successful")