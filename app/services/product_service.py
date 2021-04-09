from typing import Dict, Optional
from ..repositories import ProductRepository
from ..models import Product

class ProductService(object):
    def __init__(self, product_repository: ProductRepository, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_repository = product_repository
        
        
    def create_product(self, fields: Dict) -> Optional[Product]:
        return self.product_repository.create(fields)
    
    def get_product_by_id(self, id: int) -> Optional[Product]:
        return self.product_repository.find(id)
    
    def update_product(self, product: Product, fields: Dict):
        return self.product_repository.update(product, fields)
        
    def delete_product(self, product: Product):
        return self.product_repository.delete(product)
    
    def get_all_product(self):
        return self.product_repository.all()
        