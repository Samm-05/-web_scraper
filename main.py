from config.settings import (
    BASE_URL,
    HEADERS
)

from scraper.pipeline import Pipeline
from utils.exporter import Exporter

def main():

    scraper = Pipeline(
        HEADERS
    )

    data = scraper.run(
        BASE_URL
    )

    Exporter.to_csv(data)

    Exporter.to_json(data)

    print(
        f"Saved {len(data)} records"
    )

if __name__ == "__main__":
    main()