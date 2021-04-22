
from sqlalchemy.sql.expression import asc, desc
from .base_repository import BaseRepository
from ..models import Product
from typing import Dict
from sqlalchemy import func, or_,text


class ProductRepository(BaseRepository):
    model_class = Product

    def build_order_query(self,
                          query,
                          order: str = 'id',
                          direction: str = 'asc'
                          ):
        if direction not in ['asc', 'desc']:
            direction = 'asc'
        if direction == 'asc':
            return query.order_by(asc(self.model_class.__table__.columns[order]))
        return  query.order_by(desc(self.model_class.__table__.columns[order]))
       
    def build_filter_query(self, query, filter_dict: Dict = None):
        keys = self.model_class.__table__.columns.keys()
        filter_ = {k: filter_dict[k] for k in keys if k in filter_dict}

        if filter_:
            query = query.filter_by(**filter_)

        if 'search' in filter_dict:
            search = filter_dict.get('search').lower()
            # escape % sign

            if '%' in search:
                search = search.replace('%', '\%')

            query = query.filter(or_(
                func.lower(self.model_class.name).like('%' + search +
                                                       '%'),
                func.lower(self.model_class.description).like('%' + search +
                                                              '%')))

        return query

    def count_by_filter(self, filter_dict: Dict = None) -> int:
        query = self.build_filter_query(self.model_class.query, filter_dict)
        return query.count()