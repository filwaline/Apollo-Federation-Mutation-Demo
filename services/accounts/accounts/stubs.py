import strawberry
from strawberry.types import Info

from .graphql import User


@strawberry.federation.type(keys=["productId"])
class ReviewMutation:
    productId: str

    @strawberry.federation.field
    def currentUser(self, info: Info) -> User:
        user = info.context.repo.get_current_user()
        if user == None:
            raise ValueError("Unauthenticed User.")
        return user
