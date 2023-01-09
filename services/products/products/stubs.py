from typing import Optional, Self

import strawberry
from strawberry.types import Info

from .graphql import Product


@strawberry.federation.type(keys=["productId"])
class ReviewMutation:
    productId: str
    product: Optional[Product]

    @classmethod
    def resolve_reference(cls, info: Info, productId: str) -> Self:
        product = info.context.repo.get(productId)
        return cls(productId=productId, product=product)
