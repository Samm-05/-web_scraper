import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class Fetcher:

    def __init__(self, headers):

        self.headers = headers

        self.session = requests.Session()

        retry_strategy = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[
                429,
                500,
                502,
                503,
                504
            ]
        )

        adapter = HTTPAdapter(
            max_retries=retry_strategy
        )

        self.session.mount(
            "http://",
            adapter
        )

        self.session.mount(
            "https://",
            adapter
        )

    def get(self, url):

        response = self.session.get(
            url,
            headers=self.headers,
            timeout=10
        )

        response.raise_for_status()

        return response.text