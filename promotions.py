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

    def show_detail(self):
        return self.promotion_text

    def apply_promotion(self,product,quantity):
        pass


class ThirdOneFree(Promotion):
    def __init__(self, description):
        super().__init__(self)
        self.promotion_name = description

    def apply_promotion(self, product, quantity):
        pass



class PercentDiscount(Promotion):
    def __init__(self,description,percent):
        super().__init__(self)
        self.promotion_name = description
        self.discount = percent

    def apply_promotion(self, product, quantity):
        pass

