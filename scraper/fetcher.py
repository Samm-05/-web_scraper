import requests

class Fetcher:

    def __init__(self, headers):
        self.headers = headers

    def get(self, url):

        response = requests.get(
            url,
            headers=self.headers,
            timeout=10
        )

        response.raise_for_status()

        return response.text