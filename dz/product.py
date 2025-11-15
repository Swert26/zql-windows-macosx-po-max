class Product:
    def __init__(self, id, catrgory, in_stock, price, rating):
        self.id = id
        self.catrgory = catrgory
        self.in_stock = in_stock
        self.price = price
        self.rating = rating

class JS:
    class console:
        def log(data: str):
            print(data)
        def warn(data: str):
            print(f"⚠ {data}")
        def error(data: str):
            print(f"error {data}")