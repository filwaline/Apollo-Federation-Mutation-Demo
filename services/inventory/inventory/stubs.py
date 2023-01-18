from typing import Optional

import strawberry
from strawberry.types import Info


@strawberry.federation.type(keys=["upc"], shareable=True)
class Product:
    upc: str
    inStock: bool

    weight: int = strawberry.federation.field(external=True, default=0)
    price: int = strawberry.federation.field(external=True, default=0)

    @strawberry.federation.field(requires=["weight price"])
    def shippingEstimate(self) -> Optional[int]:
        if self.price > 1000:
            return 0
        return int(self.weight * 0.5)

    @classmethod
    def resolve_reference(cls, info: Info, upc: str, **kwargs):
        """
        when using external, the external fields are passed to resolve reference

        https://github.com/strawberry-graphql/strawberry/issues/2468#issuecomment-1387042614
        """
        p = info.context.repo.find(upc)
        if p:
            return Product(upc=p.upc, inStock=p.inStock, **kwargs)
