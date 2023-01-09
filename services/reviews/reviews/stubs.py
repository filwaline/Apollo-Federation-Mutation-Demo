from typing import List, Optional

import strawberry
from strawberry.types import Info

from .graphql import Review


@strawberry.federation.type(keys=["id"])
class User:
    id: str

    @strawberry.field
    def reviews(self, info: Info) -> List[Review]:
        return info.context.repo.find(authorId=self.id)


@strawberry.federation.type(keys=["upc"])
class Product:
    upc: str

    @strawberry.field
    def reviews(self, info: Info) -> List[Review]:
        return info.context.repo.find(productId=self.upc)
