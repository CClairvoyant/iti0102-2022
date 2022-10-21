from typing import List, Any

import pytest


class Factory:

    def __init__(self):
        self.cakes_baked = []

    def bake_cake(self, toppings: int, base: int) -> int:
        amount = 0
        if toppings == base:
            amount = toppings // 5 + toppings % 5 // 2 + toppings % 5 % 2
            self.cakes_baked += toppings // 5 * [Cake(5, 5).type]
            self.cakes_baked += toppings % 5 // 2 * [Cake(2, 2).type]
            self.cakes_baked += toppings % 5 % 2 * [Cake(1, 1).type]
        return amount

    def get_last_cakes(self, n: int) -> list:
        return self.cakes_baked[-n:]

    def get_cakes_baked(self) -> list:
        return self.cakes_baked

    def __str__(self):
        return f"{self.cakes_baked}"


class Cake:

    def __init__(self, base_amount, toppings_amount):
        allowed_list = [1, 2, 5]
        if base_amount not in allowed_list and toppings_amount not in allowed_list:
            raise WrongIngredientsAmountException("Incorrect amount of ingredients!")
        self.base_amount = base_amount
        self.toppings_amount = toppings_amount

    @property
    def type(self):
        if self.base_amount == 1 and self.toppings_amount == 1:
            return "basic"
        elif self.base_amount == 2 and self.toppings_amount == 2:
            return "medium"
        elif self.base_amount == 5 and self.toppings_amount == 5:
            return "large"

    def __repr__(self):
        return f"Cake({self.type})"

    def __eq__(self, other):
        return self.type == other.type


class WrongIngredientsAmountException(Exception):
    pass


if __name__ == '__main__':
    factory = Factory()
    factory.bake_cake(29, 29)
    print(factory.get_last_cakes(3))
    print(Factory())
