from app.views.api.responses import image
from app.models import User, Product, product
import  json

from .base_seeder import BaseSeeder


class ProductSeeder(BaseSeeder):
    def execute(self):
        data  = [
                        {
                            "name":"May tinh1",
                            "description":"May tinh1",
                            "image":"image1,image2,image3",
                            "old_price": 100000,
                            "new_price":80000
                        },
                        {
                            "name":"May tinh2",
                            "description":"May tinh2",
                            "image":"image1,image2,image3",
                            "old_price": 100000,
                            "new_price":80000
                        },
                        {
                            "name":"May tinh3",
                            "description":"May tinh3",
                            "image":"image1,image2,image3",
                            "old_price": 100000,
                            "new_price":80000
                        }
                    ]
        list_product=[]
        for item in data:
            product = Product(name=item['name'], 
                              description=item['description'],
                              image=item['image'],
                              old_price =item['old_price'], 
                              new_price= item['new_price'])
            list_product.append(product)
        self.db.session.add_all(list_product)
