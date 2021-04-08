from app.models import UserRole

from .base_repository import BaseRepository


class UserRoleRepository(BaseRepository):
    model_class = UserRole
