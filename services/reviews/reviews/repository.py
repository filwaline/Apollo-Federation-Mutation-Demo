from pydantic import BaseModel

from .graphql import Review
from .stubs import Product, User


class EmbedUser(BaseModel):
    id: str


class EmbedProduct(BaseModel):
    upc: str


class ReviewInDb(BaseModel):
    id: str
    body: str
    author: EmbedUser
    product: EmbedProduct


class ReviewRepository:
    DATA = {
        "1": ReviewInDb(
            id="1",
            body="Love it!",
            author=EmbedUser(id="1"),
            product=EmbedProduct(upc="1"),
        ),
        "2": ReviewInDb(
            id="2",
            body="Too expensive.",
            author=EmbedUser(id="1"),
            product=EmbedProduct(upc="2"),
        ),
        "3": ReviewInDb(
            id="3",
            body="Could be Better.",
            author=EmbedUser(id="2"),
            product=EmbedProduct(upc="3"),
        ),
        "4": ReviewInDb(
            id="4",
            body="Prefer something else.",
            author=EmbedUser(id="2"),
            product=EmbedProduct(upc="1"),
        ),
    }

    def comment(self, body: str, author: User, product: Product):
        id_ = str(len(self.DATA) + 1)
        review = ReviewInDb(
            id=id_,
            body=body,
            author=EmbedUser(id=author.id),
            product=EmbedProduct(upc=product.upc),
        )
        self.DATA[id_] = review
        return review

    def get(self, id_: str):
        return self.__mapping(self.DATA[id_])

    def all(self):
        return [self.__mapping(r) for r in self.DATA.values()]

    def find(self, productId=None, authorId=None, reviewId=None):
        reivews = [
            r
            for r in self.all()
            if r.product.upc == productId or r.author.id == authorId or r.id == reviewId
        ]
        return reivews

    def __mapping(self, obj: ReviewInDb) -> Review:
        return Review(
            id=obj.id,
            body=obj.body,
            author=User(id=obj.author.id),
            product=Product(upc=obj.product.upc),
        )


review_repository = ReviewRepository()
