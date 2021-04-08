from faker import Faker

from app.services import UserService

from ...mocks.repositories import MockUserRepository


class TestUserService:
    def setup_method(self, _method):
        pass

    def teardown_method(self, _method):
        pass

    def test_get_users(self):
        service = self._get_service()
        users = service.get_users(0, 10)
        assert len(users) > 0

    def test_get_user(self):
        service = self._get_service()
        user = service.get_user(123)
        assert user.id == 123

    def test_create_user(self):
        fake = Faker()
        service = self._get_service()
        email = fake.email()
        user = service.create_user({
            "email": email,
            "password": "abcde",
        })
        assert user.email == email

    def test_update_user(self):
        faker = Faker()
        email = faker.email()
        service = self._get_service()
        user = service.update_user(123, {"email": email})
        assert user.email == email

    @staticmethod
    def _get_service():
        return UserService(MockUserRepository(None))
