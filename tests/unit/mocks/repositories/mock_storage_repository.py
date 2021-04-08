from typing import Any, Dict, List, Union

from faker import Faker

from app.models import File
from app.repositories import FileRepository


class MockStorageRepository(FileRepository):
    model_class = File

    def get_model(self) -> File:
        fake = Faker()
        params: Dict = {
            "id": fake.pyint(),
            "url": fake.url(),
            "storage_type": 'local',
            "media_type": 'image',
        }
        return self.model_class(**params)

    def all(self) -> List[File]:
        return [
            self.get_model(),
            self.get_model(),
        ]

    def get(self, offset: int, limit: int, order: Any = None) -> List[File]:
        return [
            self.get_model(),
            self.get_model(),
        ]

    def create(self, fields: Dict) -> File:
        print("fields", fields)
        model = self.model_class(**fields)
        print("model", model)
        return model

    def update(self, model: File, fields: Dict) -> File:
        model = self.model_class(**fields)
        return model

    def delete(self, model: File) -> bool:
        return True

    def find(self, primary_id: Any) -> File:
        model = self.get_model()
        model.id = primary_id
        return model

    def exist(self, primary_id: Union[int, str]) -> bool:
        return True

