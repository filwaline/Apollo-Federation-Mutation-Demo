from typing import Optional

import strawberry
from strawberry.types import Info

from .stubs import Product


@strawberry.type
class Query:
    _hi: str = "hi"
