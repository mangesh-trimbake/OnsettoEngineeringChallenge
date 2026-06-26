from config import *

from client.api_client import APIClient
from client.auth import Auth
from client.banking import Banking
from client.payment import Payment


def main():

    api = APIClient()

    try:

        auth = Auth(api.client)

        print("Authenticating...")
        try :
            mfa_token = auth.login(
                EMAIL,
                PASSWORD
            )
        except Exception as error:
            print(f"An error occurred: {error}")

        print("MFA Token received")

        access_token = auth.verify_mfa(
            mfa_token,
            MFA_CODE
        )

        print("Access Token received")

        Banking(api.client).update(
            access_token,
            BANK_ROUTING,
            BANK_ACCOUNT
        )

        Payment(api.client).update(
            access_token,
            CARD_HOLDER,
            CARD_NUMBER,
            CARD_MONTH,
            CARD_YEAR,
            CARD_CVC
        )

        print("\nChallenge Completed Successfully")

    except httpx.HTTPStatusError as e:

        status = e.response.status_code

        if status == 401:
            print("Invalid credentials.")

        elif status == 403:
            print("Invalid MFA code.")

        elif status == 422:
            print("Validation failed.")
            print(e.response.text)

        elif status == 429:
            print("Rate limit exceeded.")

        else:
            print(e.response.text)

    except Exception as e:

        print(e)

    finally:

        api.close()


if __name__ == "__main__":
    import httpx
    main()