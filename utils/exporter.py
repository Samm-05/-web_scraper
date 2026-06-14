import pandas as pd
import json

class Exporter:

    @staticmethod
    def to_csv(data):

        df = pd.DataFrame(data)

        df.to_csv(
            "data/exports/books.csv",
            index=False
        )

    @staticmethod
    def to_json(data):

        with open(
            "data/exports/books.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )