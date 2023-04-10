from entity.base_storeage import BaseStorage


class Store(BaseStorage):
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)

