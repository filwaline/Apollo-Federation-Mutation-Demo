from typing import List

import strawberry
from strawberry.types import Info


@strawberry.input
class AddProductInput:
    upc: str
    name: str
    price: int
    weight: int


@strawberry.federation.type(keys=["upc"], shareable=True)
class Product:
    upc: str
    name: str
    price: int
    weight: int

    @classmethod
    def resolve_reference(cls, info: Info, upc: str):
        return info.context.repo.get(upc)


@strawberry.type
class ProductMutation:
    @strawberry.mutation
    def add(self, info: Info, input: AddProductInput) -> Product:
        product = Product(
            upc=input.upc, name=input.name, price=input.price, weight=input.weight
        )
        info.context.repo.add(product)
        return product


@strawberry.type
class Query:
    @strawberry.field
    def find_products(self, info: Info, upcs: List[str]) -> List[Product]:
        return [info.context.repo.get(upc) for upc in upcs]


@strawberry.type
class Mutation:
    @strawberry.field
    def product(self) -> ProductMutation:
        return ProductMutation()
