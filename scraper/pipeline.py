from scraper.fetcher import Fetcher
from scraper.parser import Parser
from scraper.extractor import Extractor

from utils.validator import Validator
from utils.logger import logger

class Pipeline:

    def __init__(self, headers):

        self.fetcher = Fetcher(headers)

    def run(self, url):

        logger.info(
            f"Fetching {url}"
        )

        html = self.fetcher.get(url)

        soup = Parser.parse(html)

        books = Extractor.extract_books(
            soup
        )

        valid_books = []

        for book in books:

            if Validator.validate(book):

                valid_books.append(
                    book
                )

        logger.info(
            f"Found {len(valid_books)} books"
        )

        return valid_books