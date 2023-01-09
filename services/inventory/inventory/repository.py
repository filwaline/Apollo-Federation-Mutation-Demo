from pydantic import BaseModel


class ProductInDb(BaseModel):
    upc: str
    inStock: bool


class InventoryRepository:
    DATA = {
        "1": ProductInDb(upc="1", inStock=True),
        "2": ProductInDb(upc="2", inStock=False),
        "3": ProductInDb(upc="3", inStock=True),
    }

    def find(self, upc: str):
        for p in self.DATA.values():
            if p.upc == upc:
                return p


inventory_repository = InventoryRepository()
