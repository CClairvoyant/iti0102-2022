"""Cake factory task."""


class Factory:

    """Cake factory class."""

    def __init__(self):
        """Make a list of baked cakes."""
        self.cakes_baked = []

    def bake_cake(self, toppings: int, base: int) -> int:
        """Bake large cakes if possible, then medium cakes if possible, then basic cakes, adds them to the list and
        returns the amount of cakes baked."""
        amount = 0
        if toppings == base:
            amount = toppings // 5 + toppings % 5 // 2 + toppings % 5 % 2
            self.cakes_baked += toppings // 5 * [Cake(5, 5)]
            self.cakes_baked += toppings % 5 // 2 * [Cake(2, 2)]
            self.cakes_baked += toppings % 5 % 2 * [Cake(1, 1)]
        return amount

    def get_last_cakes(self, n: int) -> list:
        """Return the last n baked cakes."""
        if n > 0:
            return self.cakes_baked[-n:]
        else:
            return []

    def get_cakes_baked(self) -> list:
        """Return the baked cakes list."""
        return self.cakes_baked

    def __str__(self):
        """Return a sentence with the amount of cakes baked."""
        if len(self.cakes_baked) == 1:
            return "Factory with 1 cake."
        else:
            return f"Factory with {len(self.cakes_baked)} cakes."


class Cake:

    """Class that is focused on assigning cake types."""

    def __init__(self, base_amount, toppings_amount):
        """Check if the amounts of bases and toppings are 1, 2 or 5."""
        allowed_list = [1, 2, 5]
        if base_amount not in allowed_list and toppings_amount not in allowed_list:
            raise WrongIngredientsAmountException("Incorrect amount of ingredients!")
        self.base_amount = base_amount
        self.toppings_amount = toppings_amount

    @property
    def type(self):
        """Find the type of cake."""
        if self.base_amount == 1 and self.toppings_amount == 1:
            return "basic"
        elif self.base_amount == 2 and self.toppings_amount == 2:
            return "medium"
        elif self.base_amount == 5 and self.toppings_amount == 5:
            return "large"

    def __repr__(self):
        """Return the cake type."""
        return f"Cake({self.type})"

    def __eq__(self, other):
        """Compare the types."""
        return self.type == other.type


class WrongIngredientsAmountException(Exception):
    """Exception triggered if the Cake class has been given the wrong amount of ingredients."""
    pass


if __name__ == '__main__':
    factory = Factory()
    print(factory)
    print(factory.bake_cake(13, 13))
    print(factory.bake_cake(2, 2))
    print(factory.get_cakes_baked())
    print(factory)
    print(Cake(1, 1))
