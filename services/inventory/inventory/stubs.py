from typing import Optional

import strawberry
from strawberry.types import Info


@strawberry.federation.type(keys=["upc"], shareable=True)
class Product:
    upc: str
    # #################################
    # # resolve_reference don't work with @external together???

    # inStock: bool

    # @classmethod
    # def resolve_reference(cls, info: Info, upc: str):
    #     p = info.context.repo.find(upc)
    #     if p:
    #         return Product(
    #             upc=p.upc,
    #             inStock=p.inStock,
    #         )

    #################################

    weight: int = strawberry.federation.field(external=True, default=0)
    price: int = strawberry.federation.field(external=True, default=0)

    @strawberry.federation.field(requires=["weight price"])
    def shippingEstimate(self) -> Optional[int]:
        if self.price > 1000:
            return 0
        return int(self.weight * 0.5)

    @strawberry.field
    def in_stock(self, info: Info) -> bool:
        p = info.context.repo.find(self.upc)
        return p.inStock if p else False
