from __future__ import annotations

from typing import List, Optional, Self

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import BaseContext, GraphQLRouter
from strawberry.types import Info

from .graphql import Mutation, Product, Query, Review, ReviewMutation, User
from .repository import review_repository

# from .stubs import Product, User


class Context(BaseContext):
    def __init__(self):
        super().__init__()
        self.repo = review_repository


def get_context():
    return Context()


schema = strawberry.federation.Schema(
    query=Query,
    mutation=Mutation,
    types=[Product, User, ReviewMutation],
    enable_federation_2=True,
)

app = FastAPI()
app.include_router(GraphQLRouter(schema, context_getter=get_context), prefix="/graphql")
