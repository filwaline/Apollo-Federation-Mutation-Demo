import strawberry
from fastapi import FastAPI
from strawberry.fastapi import BaseContext, GraphQLRouter

from .graphql import Mutation, Query, User
from .repository import account_repository
from .stubs import ReviewMutation


class Context(BaseContext):
    def __init__(self):
        super().__init__()
        self.repo = account_repository


async def get_context():
    return Context()


schema = strawberry.federation.Schema(
    query=Query,
    mutation=Mutation,
    types=[
        User,
        ReviewMutation,
    ],
    enable_federation_2=True,
)

app = FastAPI()
app.include_router(GraphQLRouter(schema, context_getter=get_context), prefix="/graphql")
