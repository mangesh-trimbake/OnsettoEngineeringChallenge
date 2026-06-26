from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)

    def login(self,email,password):

        self.driver.get("https://marketplace.dev-challenge.com/login")

        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID,"email")
            )
        ).send_keys(email)

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys(password)

        self.driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def verify_mfa(self,code):

        otp = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "input[data-input-otp='true']"
                )
            )
        )

        otp.send_keys(code)

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[text()='Verify']"
                )
            )
        ).click()

        self.wait.until(
            EC.url_contains("/app/marketplace")
        )