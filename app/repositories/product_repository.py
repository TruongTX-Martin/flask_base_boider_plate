
from .base_repository import BaseRepository
from ..models import Product

class ProductRepository(BaseRepository):
    model_class = Product