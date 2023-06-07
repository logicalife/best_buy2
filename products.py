class Product():
    """This class is for the product with name, price and quantity
      as initializers"""
    def __init__(self,name,price,quantity):
      self.name = name
      self.price = price
      self.quantity = quantity
      self.active = True

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
      return f"{self.name} , Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, buy_quantity):
      """This method accepts quntity of item and if stock available, it deducts from stock
         and returns value"""
      if buy_quantity > self.quantity:
        print("Not enough quantity available")
      else:
        self.quantity -= buy_quantity
        if self.quantity <= 0:
          self.deactivate()
        return self.price*buy_quantity
