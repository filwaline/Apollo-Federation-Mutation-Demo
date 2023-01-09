from typing import List, Optional

import strawberry
from strawberry.types.info import Info


@strawberry.federation.type(keys=["id"])
class User:
    id: str
    name: Optional[str]
    username: Optional[str]
    birthDate: Optional[str]

    @classmethod
    def resolve_reference(cls, info: Info, id: str):
        return info.context.repo.get(id)


@strawberry.type
class Query:
    @strawberry.field
    def me(self, info: Info) -> User:
        user = info.context.repo.get_current_user()
        if not user:
            raise ValueError("Unauthenticated User.")
        return user


@strawberry.type
class Mutation:
    @strawberry.mutation
    def login(self, info: Info, username: str) -> User:  # demo only, don't do this!
        user = info.context.repo.login(username)
        if not user:
            raise ValueError("Unknown User.")
        return user
