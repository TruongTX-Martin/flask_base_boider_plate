from app.repositories.product_repository import ProductRepository
from flask import Blueprint, request
from ....middlewares.authenticate import token_required
from injector  import inject
from app.exceptions import (NotFoundError, LogicError)
from app.services import ProductService
from ..schemas import CreateProductSchema
from ..responses import (Product, Status, Products)


app = Blueprint('api.product', __name__)



@app.route('', methods=['GET'])
@inject
@token_required
def get_product(product_service: ProductService, product_repository: ProductRepository):
    search = request.args.get('search')
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', default=10, type=int)
    order = request.args.get('order', default='id')
    direction = request.args.get('direction', default='asc')
    filter_dict = {}
    print('Show parameter offset:', offset)
    if search:
        filter_dict['search'] = search
    if order:
        filter_dict['order'] = order
    filter_dict['offset'] = offset
    filter_dict['limit'] = limit
    products = product_repository.get_by_filter(filter_dict=filter_dict,
                                          offset=offset,
                                          limit=limit,
                                          order=filter_dict['order'],
                                          direction=direction)
    total_count = product_repository.count_by_filter(filter_dict=filter_dict)
    return Products(models=products,total_count=total_count,
                 offset=offset,
                 limit=limit).response()
    

# create product
@app.route('', methods=['POST'])
@inject
@token_required
def create(product_service: ProductService):
    request_data = request.get_json()
    CreateProductSchema().load(request_data);
    product = product_service.create_product(request_data)
    return Product(product).response();
    

# update product
@app.route('/<product_id>', methods=['PUT'])
@inject
@token_required
def update(product_id, product_service: ProductService):
    request_data = request.get_json()
    CreateProductSchema().load(request_data);
    product = product_service.get_product_by_id(product_id)
    product = product_service.update_product(product,request_data)
    return Product(product).response();
    
    
#delete product
@app.route('/<product_id>', methods=['DELETE'])
@inject
@token_required
def delete(product_id,product_service: ProductService):
    product = product_service.get_product_by_id(product_id)
    if product is None:
        raise NotFoundError("Product id = {} not found".format(product_id))
    
    deleted = product_service.delete_product(product)
    
    if not deleted:
        raise LogicError(
            "Delete poll id = {} not successfully".format(product_id))

    return Status("Delete poll successfully").response()
    
    