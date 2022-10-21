class Factory:
    def __init__(self):
        pass

    def bake_cake(self, toppings: int, base: int) -> int:
        pass

    def get_last_cakes(self, n: int) -> list:
        pass

    def get_cakes_baked(self) -> list:
        pass

    def __str__(self):
        pass


class Cake:

    def __init__(self, base_amount, toppings_amount):
        self.base_amount = base_amount
        self.toppings_amount = toppings_amount

    @property
    def type(self):
        if self.base_amount == 1 and self.toppings_amount == 1:
            return "basic"
        elif 2 <= self.base_amount <= 4 and 2 <= self.toppings_amount <= 4:
            return "medium"
        else:
            return "large"

    def __repr__(self):
        return f"Cake{self.type}"

    def __eq__(self, other):
        return self.type == other.type


class WrongIngredientsAmountException(Exception):
    pass
