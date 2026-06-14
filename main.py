from config.settings import HEADERS
from scraper.pipeline import Pipeline
from utils.exporter import Exporter

import time
import random

def main():

    scraper = Pipeline(HEADERS)

    all_books = []

    for page in range(1, 6):

        url = (
            f"https://books.toscrape.com/"
            f"catalogue/page-{page}.html"
        )

        books = scraper.run(url)

        all_books.extend(books)

        # Rate limiting (wait 1–3 seconds)
        sleep_time = random.uniform(1, 3)

        print(
            f"Waiting {sleep_time:.2f} seconds..."
        )

        time.sleep(sleep_time)

    Exporter.to_csv(all_books)

    Exporter.to_json(all_books)

    print(
        f"\nSaved {len(all_books)} books"
    )

if __name__ == "__main__":
    main()