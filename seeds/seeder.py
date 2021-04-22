import os

from .user_seeder import UserSeeder
from .product_seeder import  ProductSeeder


class Seeder:
    def __init__(self, db):
        self.db = db

    def execute(self):
        # UserSeeder(db=self.db).execute()
        ProductSeeder(db=self.db).execute()

        # if os.getenv('FLASK_ENV') is 'development':
        #     PollSeeder(db=self.db).execute()
