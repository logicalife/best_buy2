from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self,product,quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, promotion_text):
        super().__init__(self)
        self.promotion_text = promotion_text

    def apply_promotion(self,price,quantity):
        if quantity == 1:
            return price*quantity
        elif quantity %2 ==0:
            return price*0.75*quantity
        else:
            return (quantity-1)*price*0.75 + price

    def __repr__(self):
        return self.promotion_text



class ThirdOneFree(Promotion):
    def __init__(self, description):
        super().__init__(self)
        self.promotion_text = description

    def apply_promotion(self, price, quantity):
        if quantity == 1 or quantity == 2:
            return price*quantity
        if quantity % 3 == 0:
            quantity -= quantity/3
            return price*quantity
        else:
            quantity -= int(quantity/3)
            return price*quantity

    def __repr__(self):
        return self.promotion_text



class PercentDiscount(Promotion):
    def __init__(self, description, percent):
        super().__init__(self)
        self.promotion_text = description
        self.discount = int(percent)/100

    def apply_promotion(self, price, quantity):
        return price*(1-self.discount)*quantity

    def __repr__(self):
        return self.promotion_text
