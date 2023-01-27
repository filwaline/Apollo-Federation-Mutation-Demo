from __future__ import annotations

from typing import List

import strawberry
from strawberry.types import Info


@strawberry.federation.type(keys=["id"])
class Review:
    id: str
    body: str
    author: User
    product: Product


@strawberry.federation.type(keys=["productId"])
class ReviewMutation:
    productId: str
    product: Product = strawberry.federation.field(external=True, default=None)
    currentUser: User = strawberry.federation.field(external=True, default=None)

    @strawberry.federation.mutation(requires=["product{upc} currentUser{id}"])
    def comment(self, info: Info, body: str) -> Review:

        review = info.context.repo.comment(
            body=body, product=self.product, author=self.currentUser
        )
        return review


@strawberry.type
class Query:
    @strawberry.field
    def find_reviews(self, info: Info, ids: List[str]) -> List[Review]:
        return [info.context.repo.get(id_) for id_ in ids]


@strawberry.type
class Mutation:
    @strawberry.field
    def review(self, productId: str) -> ReviewMutation:
        """
        You may query other subgraph's data for mutation now.

        And the price is:
            - you must declare what you need here, rather pack all parameters in one input type.
            - you must define some stubs in other subgraph, so they can resolve your requires before mutation.
                - package.products.stubs.ReviewMutation
                - package.accounts.stubs.ReviewMutation
        """
        return ReviewMutation(productId=productId)


from .stubs import Product, User
