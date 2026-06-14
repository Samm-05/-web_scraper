from config.settings import HEADERS
from scraper.pipeline import Pipeline
from utils.exporter import Exporter
from database.crud import save_books

import argparse
import time
import random


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--pages",
        type=int,
        default=5,
        help="Number of pages to scrape"
    )

    args = parser.parse_args()

    scraper = Pipeline(
        HEADERS
    )

    all_books = []

    for page in range(1, args.pages + 1):

        url = (
            f"https://books.toscrape.com/"
            f"catalogue/page-{page}.html"
        )

        books = scraper.run(url)

        all_books.extend(
            books
        )

        sleep_time = random.uniform(
            1,
            3
        )

        print(
            f"Waiting {sleep_time:.2f}s..."
        )

        time.sleep(
            sleep_time
        )

    save_books(
        all_books
    )

    Exporter.to_csv(
        all_books
    )

    Exporter.to_json(
        all_books
    )

    print(
        f"\nSaved {len(all_books)} books"
    )


if __name__ == "__main__":
    main()