from datetime import datetime


class Products:
    '''Products class for creating product instances'''
    products_list = {}
    
    def __init__(self, name, category, quantity, price):
        self.id = len(Products.products_list) + 1
        self.product_name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.datecreated = str(datetime.now())

    def new_product(self):
        new_product_name = self.product_name
        Products.products_list[self.product_name] = self.__dict__

    def update_product(self, *args):
        self.quantity += quantity
        updated_product = self.product_name
        Products.products_list[self.product_name] = self.__dict__

    def get_all(self):
        return Products.products_list