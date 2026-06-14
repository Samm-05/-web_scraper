from bs4 import BeautifulSoup

class Parser:

    @staticmethod
    def parse(html):

        return BeautifulSoup(
            html,
            "html.parser"
        )