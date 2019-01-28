from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
# from flask_jwt_extended import jwt_required

from ..models.products_model import Products

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('product_name', required = True, help = 'Product name is required')
parser.add_argument('category', required = True, help = 'Product name is required')
parser.add_argument('quantity', required = True, help = 'quantity of product is required')
parser.add_argument('price', required = True, help = 'Please set product price')


class AllProducts(Resource):
    '''Get method for fetching all products'''
    @jwt_required()
    def get(self):
        products = Products.get_all(self)
        return {'Products': products}
        
    @jwt_required()
    def post(self):
        args = parser.parse_args()
        name = args['product_name']
        category = args['category']
        quantity = args['quantity']
        price = args['price']
        
        if len(args) > 4:
            return { 'Error':'can only take name, category, price, quantity' }

        new_product = Products(name, category, quantity, price)
        new_product.new_product()
        return {'New product created': Products.products_list[name]}, 201
        