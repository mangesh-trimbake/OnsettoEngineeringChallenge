from config import API_BASE_URL


class Payment:

    def __init__(self, client):
        self.client = client

    def update(
        self,
        token,
        holder,
        number,
        month,
        year,
        cvc
    ):

        response = self.client.put(
            f"{API_BASE_URL}/account/payment",
            headers={
                "Authorization": f"Bearer {token}"
            },
            json={
                "cardholder_name": holder,
                "card_number": number,
                "exp_month": month,
                "exp_year": year,
                "cvc": cvc
            }
        )

        response.raise_for_status()

        data = response.json()

        print("\nPayment Updated")

        print("Brand :", data["card_brand"])
        print("Last4 :", data["last4"])
        print("Expiry:", f'{data["exp_month"]}/{data["exp_year"]}')