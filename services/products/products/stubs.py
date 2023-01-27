import strawberry
from strawberry.types import Info

from .graphql import Product


@strawberry.federation.type(keys=["productId"])
class ReviewMutation:
    productId: str

    @strawberry.field
    def product(self, info: Info) -> Product:
        product = info.context.repo.get(self.productId)
        if product == None:
            raise ValueError("Product Not Found.")
        return product
