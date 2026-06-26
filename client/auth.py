from config import API_BASE_URL


class Auth:

    def __init__(self, client):
        self.client = client

    def login(self, email, password):
        response = self.client.post(
            f"{API_BASE_URL}/auth/token",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "email": email,
                "password": password
            }
        )

        # print("Status:", response.status_code)
        # print("Headers:", response.headers)
        # print("Body:")
        # print(response.text)
        response.raise_for_status()

        return response.json()["mfa_token"]

    def verify_mfa(self, mfa_token, code):
        response = self.client.post(
            f"{API_BASE_URL}/auth/mfa/verify",
            json={
                "mfa_token": mfa_token,
                "code": code
            }
        )

        response.raise_for_status()

        return response.json()["access_token"]