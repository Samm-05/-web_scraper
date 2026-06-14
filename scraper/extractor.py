class Extractor:

    @staticmethod
    def extract_books(soup):

        books = []

        cards = soup.select(
            ".product_pod"
        )

        for card in cards:

            title = card.h3.a["title"]

            price = card.select_one(
                ".price_color"
            ).text

            books.append({
                "title": title,
                "price": price
            })

        return books