from typing import Any, Dict, List, Optional, Union

from sqlalchemy import and_, or_

from app.models import File

from ..database import db
from .base_repository import BaseRepository


class FileRepository(BaseRepository):
    model_class = File

    def find_additional(self, url: str, media_type) -> db.Model:
        return self.model_class.query.filter_by(
            url=url,
            media_type=media_type,
            storage_type=File.STORAGE.ADDITIONAL,
        ).first()
