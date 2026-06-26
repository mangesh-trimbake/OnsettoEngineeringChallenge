from config import API_BASE_URL


class Banking:

    def __init__(self, client):
        self.client = client

    def update(self, token, routing, account):

        response = self.client.put(
            f"{API_BASE_URL}/account/banking",
            headers={
                "Authorization": f"Bearer {token}"
            },
            json={
                "routing_number": routing,
                "account_number": account
            }
        )

        response.raise_for_status()

        data = response.json()

        print("\nBank Updated")

        print("Routing :", data["routing_masked"])
        print("Account :", data["account_masked"])