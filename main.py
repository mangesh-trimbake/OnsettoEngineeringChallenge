from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

EMAIL = "candidate1@onsetto.test"
PASSWORD = "Password123!"
MFA = "1234"        # <-- Replace with actual code

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

wait = WebDriverWait(driver,20)

driver.maximize_window()

driver.get("https://marketplace.dev-challenge.com/login")

#
# Login
#

wait.until(
    EC.visibility_of_element_located((By.ID,"email"))
).send_keys(EMAIL)

driver.find_element(By.ID,"password").send_keys(PASSWORD)

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()

#
# MFA
#

otp = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR,"input[data-input-otp='true']")
    )
)

otp.send_keys(MFA)

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,"//button[text()='Verify']")
    )
).click()

#
# Wait Account page
#

# wait.until(
#     EC.presence_of_element_located(
#         (By.ID,"bank-routing")
#     )
# )

#####################################

# Wait until marketplace page loads
wait.until(
    EC.url_contains("/app/marketplace")
)

# Click Account
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/app/account']")
    )
).click()

# Wait until account page opens
wait.until(
    EC.url_contains("/app/account")
)


###################################

#
# Banking
#

driver.find_element(By.ID,"bank-routing").send_keys("123456789")

driver.find_element(By.ID,"bank-account").send_keys("987654321012")

driver.find_element(By.ID,"bank-save").click()

#
# Payment
#

driver.find_element(By.ID,"card-holder").send_keys("John Doe")

driver.find_element(By.ID,"card-number").send_keys("4242424242424242")

driver.find_element(By.ID,"card-exp-month").send_keys("12")

driver.find_element(By.ID,"card-exp-year").send_keys("2032")

driver.find_element(By.ID,"card-cvc").send_keys("123")

driver.find_element(By.ID,"card-save").click()

#
# Verify
#

bank_summary = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,"[data-testid='bank-saved-info']")
    )
).text

payment_summary = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,"[data-testid='payment-saved-info']")
    )
).text

print(bank_summary)
print(payment_summary)

print("SUCCESS")

input("Press Enter to exit...")

driver.quit()