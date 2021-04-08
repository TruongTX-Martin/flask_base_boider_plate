from typing import Any, Dict, List, Union

from faker import Faker

from app.models import User
from app.repositories import UserRepository


class MockUserRepository(UserRepository):
    model_class = User

    def get_model(self) -> User:
        fake = Faker()
        params: Dict = {
            "id": fake.pyint(),
            "email": fake.email(),
        }
        return self.model_class(**params)

    def all(self) -> List[User]:
        return [
            self.get_model(),
            self.get_model(),
        ]

    def get(self, offset: int, limit: int, order: Any = None) -> List[User]:
        return [
            self.get_model(),
            self.get_model(),
        ]

    def create(self, fields: Dict) -> User:
        model = self.model_class(**fields)
        return model

    def update(self, model: User, fields: Dict) -> User:
        model = self.model_class(**fields)
        return model

    def delete(self, model: User) -> bool:
        return True

    def find(self, primary_id: Any) -> User:
        model = self.get_model()
        model.id = primary_id
        return model

    def exist(self, primary_id: Union[int, str]) -> bool:
        return True

    def get_user_by_email(self, email: str) -> User:
        model = self.get_model()
        if model.email is email:
            return model
        return None
