from typing import Optional

from app.models import User

from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    model_class = User

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.model_class.query.filter_by(email=email).first()

    def find_by_anonymous_id(self, anonymous_id) -> Optional[User]:
        return self.model_class.query.filter_by(
            anonymous_id=anonymous_id).first()
