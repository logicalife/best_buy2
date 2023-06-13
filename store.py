class Store():
    """Class for the store with product_list as initializer """
    def __init__(self,product_list):
      self.list_of_products = product_list

    def add_product(self,product):
        """To add new product in the store object"""
        self.list_of_products.append(product)

    def remove_product(self, product):
        """To remove existing product in the store object"""
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        """Returns total item available in store"""
        total_qty = 0
        for item in self.list_of_products:
            if item.is_active():
                total_qty += item.quantity
        return total_qty

    def get_all_products(self):
        """To get allt he active product"""
        active_product = []
        for item in self.list_of_products:
            if item.is_active() is True:
                active_product.append(item)
        return active_product

    def order(self, shopping_list):
        """Performs order task according to shopping list"""
        total = 0
        for item,quantity in shopping_list:
            total += item.buy(quantity)
        return total
