from __future__ import annotations

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import BaseContext, GraphQLRouter

from .graphql import Mutation, Product, Query
from .repository import product_repository
from .stubs import ReviewMutation


class Context(BaseContext):
    def __init__(self):
        super().__init__()
        self.repo = product_repository


def get_context():
    return Context()


schema = strawberry.federation.Schema(
    query=Query,
    mutation=Mutation,
    types=[Product, ReviewMutation],
    enable_federation_2=True,
)

app = FastAPI()
app.include_router(GraphQLRouter(schema, context_getter=get_context), prefix="/graphql")
