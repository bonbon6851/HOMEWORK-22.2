from entity.base_storeage import BaseStorage
from exceptions import DifferentProduct


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:

        if name not in self.get_items() and self.get_unique_items_count() >= 5:
            raise DifferentProduct
        super().add(name, amount)
