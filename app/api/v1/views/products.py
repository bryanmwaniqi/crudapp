from flask_restful import Resource, reqparse

from ..models.products_model import Products

parser = reqparse.RequestParser()
parser.add_argument('name', required = True, help = 'Product name is required')
parser.add_argument('category', required = True, help = 'Product name is required')
parser.add_argument('quantity', required = True, help = 'quantity of product is required')
parser.add_argument('price', required = True, help = 'Please set product price')


class AllProducts(Resource):
    '''Get method for fetching all products'''
    def get(self):
        products = Products.get_all(self)
        return {'Products': products}

    def post(self):
        args = parser.parse_args()
        name = args['name']
        category = args['category']
        quantity = args['quantity']
        price = args['price']
        
        if len(args) > 4:
            return { 'Error':'can only take name, category, price, quantity' }

        if name in Products.products_list.keys():
            product = Products.products_list['name']
            product.update_product(name, category, quantity, price)
            return 'Existing Product has been updated', 200
        else:
            new_product = Products(name, category, quantity, price)
            new_product.new_product()
            return {'New product created': Products.products_list}, 201
        