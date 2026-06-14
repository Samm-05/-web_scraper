from config.settings import HEADERS
from scraper.pipeline import Pipeline
from utils.exporter import Exporter

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

    Exporter.to_csv(all_books)
    Exporter.to_json(all_books)

    print(
        f"Saved {len(all_books)} books"
    )

if __name__ == "__main__":
    main()