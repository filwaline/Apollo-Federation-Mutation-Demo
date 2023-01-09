from dataclass_mapper import map_to, mapper
from pydantic import BaseModel

from .graphql import User


@mapper(User)
class UserInDb(BaseModel):
    id: str
    name: str
    birthDate: str
    username: str


class AccountRepository:
    DATA = {
        "1": UserInDb(
            id="1", name="Ada Lovelace", birthDate="1815-12-10", username="@ada"
        ),
        "2": UserInDb(
            id="2", name="Alan Turing", birthDate="1912-06-23", username="@complete"
        ),
    }
    CURRENT_USER = None

    def login(self, username: str):
        user = None
        for u in self.DATA.values():
            if u.username == username:
                user = u
                break

        self.CURRENT_USER = user
        if user:
            return map_to(user, User)

    def get_current_user(self):
        if self.CURRENT_USER:
            return map_to(self.CURRENT_USER, User)

    def get(self, id: str):
        return map_to(self.DATA[id], User)


account_repository = AccountRepository()
