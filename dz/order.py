class Order:
    def __init__(self, id: str, date: str, status: str, total: int, items: list):
        self.id = id
        self.date = date
        self.status = status
        self.total = total
        self.items = items