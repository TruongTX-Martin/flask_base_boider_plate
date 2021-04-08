from app.models import User

from .base_seeder import BaseSeeder


class UserSeeder(BaseSeeder):
    def execute(self):
        admin_user = User(id=1, email="admin@example.com", password="testtest")
        self.db.session.add(admin_user)
