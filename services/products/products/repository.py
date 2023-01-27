from dataclass_mapper import map_to, mapper, mapper_from
from pydantic import BaseModel

from .graphql import Mutation, Product, Query
from .stubs import ReviewMutation


@mapper(Product)
@mapper_from(Product)
class ProductInDb(BaseModel):
    upc: str
    name: str
    price: int
    weight: int


class ProductRepository:
    DATA = {
        "1": ProductInDb(upc="1", name="Table", price=899, weight=100),
        "2": ProductInDb(upc="2", name="Couch", price=1299, weight=1000),
        "3": ProductInDb(upc="3", name="Chair", price=54, weight=50),
    }

    def all(self):
        return [map_to(p, Product) for p in self.DATA.values()]

    def get(self, upc):
        if upc in self.DATA:
            return map_to(self.DATA[upc], Product)
        return None

    def add(self, p: Product):
        if p.upc not in self.DATA:
            self.DATA[p.upc] = map_to(p, ProductInDb)


product_repository = ProductRepository()
