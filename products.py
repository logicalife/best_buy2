from promotions import Promotion

class Product:
    """This class is for the product with name, price and quantity
      as initializers"""
    def __init__(self, name, price, quantity):
        try:
            self.name = name
            self.price = float(price)
            self.quantity = int(quantity)
            self.active = True
            self.promotion = None
        except:
            raise ValueError()

    def get_quantity(self):
        """Return quantity of perticular item in the store"""
        return self.quantity

    def set_quantity(self, quantity):
      """This function manually sets defined quantity of existing item"""
      self.quantity = quantity
      if self.quantity <= 0:
        self.deactivate()

    def is_active(self):
      """This method checks the perticular itemis active or not"""
      if self.quantity >= 1:
        return True
      else:
        self.deactivate()
        return False

    def activate(self):
      """To activate item"""
      self.active = True

    def deactivate(self):
      """To deactivate item"""
      self.active = False

    def show(self):
      """To show all the product with name,price and quantity"""
      return f"{self.name} , Price: {self.price}, Quantity: {self.quantity}, Promotion : {self.get_promotion()}"

    def buy(self, buy_quantity):
      """This method accepts quntity of item and if stock available, it deducts from stock
         and returns value"""
      if buy_quantity > self.quantity:
          raise Exception("Not enough quantity available")
      else:
        self.quantity -= buy_quantity
        if self.quantity <= 0:
            self.deactivate()
        if self.get_promotion() == "None":
            return self.price*buy_quantity
        else:
            return self.promotion.apply_promotion(self.price, buy_quantity)

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
      """To show all the product with name,price and quantity"""
      return f"{self.name} , Price: {self.price}, Quantity : Unlimited, Promotion : {self.get_promotion()}"

    def is_active(self):
        return True

    def buy(self, buy_quantity):
        """This method accepts quntity of item and if stock available, it deducts from stock
         and returns value"""
        if self.get_promotion() == "None":
            return self.price * buy_quantity
        else:
            return self.promotion.apply_promotion(self.price, buy_quantity)


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = int(maximum)

    def show(self):
        """To show all the product with name,price and quantity"""
        return f"{self.name} , Price: {self.price}, Limited to {self.maximum} per order!,Promotion : {self.get_promotion()}"




