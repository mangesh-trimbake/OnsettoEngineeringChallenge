import httpx


class APIClient:

    def __init__(self):
        self.client = httpx.Client(timeout=30)

    def post(self, url, **kwargs):
        return self.client.post(url, **kwargs)

    def put(self, url, **kwargs):
        return self.client.put(url, **kwargs)

    def close(self):
        self.client.close()