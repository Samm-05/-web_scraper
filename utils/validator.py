class Validator:

    @staticmethod
    def validate(item):

        return (
            item["title"] != ""
            and item["price"] != ""
        )