"""Alchemy."""


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """

    def __init__(self, name: str):
        """Initialize the AlchemicalElement class."""
        self.name = name

    def __repr__(self):
        """Representation of the AlchemicalElement class."""
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.elements = []

    def add(self, element):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError
        exception.

        :param element: Input object to add to storage.
        """
        if type(element) in [AlchemicalElement, Catalyst]:
            self.elements.append(element)
        else:
            raise TypeError

    def pop(self, element_name: str) -> AlchemicalElement or None:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        name_list = []
        for element in self.elements:
            name_list.append(element.name)
        if element_name in name_list:
            return self.elements.pop(name_list[::-1].index(element_name) - 1)
        return None

    def extract(self) -> list[AlchemicalElement]:
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
        storage = AlchemicalStorage()
        storage.add(AlchemicalElement('Water'))
        storage.add(AlchemicalElement('Fire'))
        storage.extract() # -> [<AE: Water>, <AE: Fire>]
        storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        new_list = self.elements.copy()
        self.elements = []
        return new_list

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        :return: Content as a string.
        """
        content = "Content:"
        if not self.elements:
            content += "\n Empty."
        name_list = []
        for element in self.elements:
            name_list.append(element.name)
        for name in sorted(name_list):
            if name not in content:
                content += f"\n * {name} x {name_list.count(name)}"
        return content


class AlchemicalRecipes:
    """AlchemicalRecipes class."""

    def __init__(self):
        """
        Initialize the AlchemicalRecipes class.

        Add whatever you need to make this class function.
        """
        self.recipe_book = []

    def add_recipe(self, first_component_name: str, second_component_name: str, product_name: str):
        """
        Determine if recipe is valid and then add it to recipes.

        A recipe consists of three strings, two components and their product.
        If any of the parameters are the same, raise the 'DuplicateRecipeNamesException' exception.
        If there already exists a recipe for the given pair of components, raise the 'RecipeOverlapException' exception.

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :param product_name: The name of the product element.
        """
        if len({first_component_name, second_component_name, product_name}) < 3:
            raise DuplicateRecipeNamesException
        for recipe in self.recipe_book:
            if f"{first_component_name} + {second_component_name}" == recipe.split(" =")[0] or \
                    f"{second_component_name} + {first_component_name}" == recipe.split(" =")[0]:
                raise RecipeOverlapException
        else:
            self.recipe_book.append(f"{first_component_name} + {second_component_name} = {product_name}")

    def get_product_name(self, first_component_name: str, second_component_name: str) -> str or None:
        """
        Return the name of the product for the two components.

        The order of the first_component_name and second_component_name is interchangeable, so search for combinations
        of (first_component_name, second_component_name) and (second_component_name, first_component_name).

        If there are no combinations for the two components, return None

        Example:
        recipes = AlchemicalRecipes()
        recipes.add_recipe('Water', 'Wind', 'Ice')
        recipes.get_product_name('Water', 'Wind')  # ->  'Ice'
        recipes.get_product_name('Wind', 'Water')  # ->  'Ice'
        recipes.get_product_name('Fire', 'Water')  # ->  None
        recipes.add_recipe('Water', 'Fire', 'Steam')
        recipes.get_product_name('Fire', 'Water')  # ->  'Steam'

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :return: The name of the product element or None.
        """
        for recipe in self.recipe_book:
            if f"{first_component_name} + {second_component_name}" in recipe or \
                    f"{second_component_name} + {first_component_name}" in recipe:
                return recipe.split(" = ")[-1]
        else:
            return None

    def get_component_names(self, product_name: str) -> tuple[str, str] or None:
        """Return the components required to make a product."""
        for recipe in self.recipe_book:
            if product_name == recipe.split("= ")[-1]:
                return recipe.split(" +")[0], recipe.split(" =")[0].split("+ ")[-1]
        else:
            return None


class DuplicateRecipeNamesException(Exception):
    """Raised when attempting to add a recipe that has same names for components and product."""


class RecipeOverlapException(Exception):
    """Raised when attempting to add a pair of components that is already used for another existing recipe."""


class Cauldron(AlchemicalStorage):
    """
    Cauldron class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Cauldron class."""
        super(Cauldron, self).__init__()
        self.recipes = recipes

    def add(self, element):
        """
        Add element to storage and check if it can combine with anything already inside.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Exam
        recipes = AlchemicalRecipes()
        recipes.add_recipe('Water', 'Wind', 'Ice')
        cauldron = Cauldron(recipes)
        cauldron.add(AlchemicalElement('Water'))
        cauldron.add(AlchemicalElement('Wind'))
        cauldron.extract() # -> [<AE: Ice>]

        :param element: Input object to add to storage.
        """
        if type(element) not in [AlchemicalElement, Catalyst]:
            raise TypeError
        for recipe in self.recipes.recipe_book:
            for i in range(len(self.elements)):
                if f"{self.elements[-i - 1].name} + {element.name}" == recipe.split(" =")[0] or f"{element.name} + " \
                        f"{self.elements[-i - 1].name}" == recipe.split(" =")[0]:
                    if type(element) is AlchemicalElement:
                        if type(self.elements[-i - 1]) is AlchemicalElement:
                            self.elements.pop(-i - 1)
                            self.add(AlchemicalElement(recipe.split("= ")[-1]))
                            return
                        elif self.elements[-i - 1].uses > 0:
                            self.elements[-i - 1].uses -= 1
                            self.add(AlchemicalElement(recipe.split("= ")[-1]))
                            return
                    else:
                        if type(self.elements[-i - 1]) is AlchemicalElement and element.uses > 0:
                            self.elements.pop(-i - 1)
                            element.uses -= 1
                            super().add(element)
                            self.add(AlchemicalElement(recipe.split("= ")[-1]))
                            return
                        elif element.uses > 0 and self.elements[-i - 1].uses > 0:
                            element.uses -= 1
                            self.elements[-i - 1].uses -= 1
                            super().add(element)
                            self.add(AlchemicalElement(recipe.split("= ")[-1]))
                            return
        else:
            super().add(element)


class Catalyst(AlchemicalElement):
    """Catalyst class."""

    def __init__(self, name: str, uses: int):
        """
        Initialize the Catalyst class.

        :param name: The name of the Catalyst.
        :param uses: The number of uses the Catalyst has.
        """
        super().__init__(name)
        self.uses = uses

    def __repr__(self) -> str:
        """
        Representation of the Catalyst class.

        Example:
            catalyst = Catalyst("Philosophers' stone", 3)
            print(catalyst) # -> <C: Philosophers' stone (3)>

        :return: String representation of the Catalyst.
        """
        return f"<C: {self.name} ({self.uses})>"


class Purifier(AlchemicalStorage):
    """
    Purifier class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Purifier class."""
        super().__init__()
        self.recipes = recipes

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can be split into anything.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            purifier = Purifier(recipes)
            purifier.add(AlchemicalElement('Ice'))
            purifier.extract() # -> [<AE: Water>, <AE: Wind>]   or  [<AE: Wind>, <AE: Water>]

        :param element: Input object to add to storage.
        """
        if type(element) in [AlchemicalElement, Catalyst]:
            for recipe in self.recipes.recipe_book:
                if element.name in recipe.split("= ")[-1]:
                    super().add(AlchemicalElement(self.recipes.get_component_names(recipe.split("= ")[-1])[0]))
                    super().add(AlchemicalElement(self.recipes.get_component_names(recipe.split("= ")[-1])[1]))
                    return
            else:
                super().add(element)
        else:
            raise TypeError


if __name__ == '__main__':
    recipes = AlchemicalRecipes()
    recipes.add_recipe("A", "B", "AB")
    recipes.add_recipe("A", "C", "AC")
    recipes.add_recipe("B", "C", "BC")
    recipes.add_recipe("A", "D", "AD")
    recipes.add_recipe("B", "D", "BD")
    recipes.add_recipe("C", "D", "CD")
    recipes.add_recipe("A", "E", "AE")
    recipes.add_recipe("B", "E", "BE")
    recipes.add_recipe("C", "E", "CE")
    recipes.add_recipe("D", "E", "DE")
    recipes.add_recipe("AB", "CD", "ABCD")
    recipes.add_recipe("BC", "DE", "BCDE")
    recipes.add_recipe("AB", "DE", "ABDE")
    recipes.add_recipe("ABC", "DE", "ABCDE")
    recipes.add_recipe("ABC", "D", "ABCD")
    recipes.add_recipe("AB", "C", "ABC")
    recipes.add_recipe("AB", "D", "ABD")
    recipes.add_recipe("AB", "E", "ABE")
    recipes.add_recipe("AC", "DE", "ACDE")
    recipes.add_recipe("AB", "CE", "ABCE")
    recipes.add_recipe("BC", "D", "BCD")
    recipes.add_recipe("BC", "E", "BCE")
    recipes.add_recipe("BD", "E", "BDE")
    recipes.add_recipe("BE", "CD", "BECD")
    recipes.add_recipe("CD", "E", "CDE")
    cauldron = Cauldron(recipes)
    cauldron.add(AlchemicalElement("A"))
    print(cauldron.get_content())
    cauldron.add(AlchemicalElement("B"))
    print(cauldron.get_content())
    cauldron.add(AlchemicalElement("C"))
    print(cauldron.get_content())
    cauldron.add(AlchemicalElement("E"))
    print(cauldron.get_content())
    cauldron.add(AlchemicalElement("D"))
    print(cauldron.get_content())



    # recipes.add_recipe("Philosophers' stone", 'Mercury', 'Gold')
    # recipes.add_recipe("Earth", "Fire", "Philosophers' stone")
    # purifier = Purifier(recipes)
    # purifier.add(AlchemicalElement("Gold"))
    # print(purifier.get_content())
    # purifier.add(Catalyst("Philosophers' stone", 3))
    # print(purifier.get_content())

    # recipes.add_recipe("Earth", "Fire", "Result")
    # recipes.add_recipe("Steam", "Dirt", "Mud")
    # recipes.add_recipe("Water", "Result", "Steam")
    # purifier = Purifier(recipes)
    # purifier.add(AlchemicalElement("Earth"))
    # print(purifier.get_content())
    # purifier.add(AlchemicalElement("Mud"))
    # print(purifier.get_content())
    # purifier.add(AlchemicalElement("Mud"))
    # print(purifier.get_content())
    # purifier.add(AlchemicalElement("Mud"))
    # print(purifier.get_content())

    # recipes = AlchemicalRecipes()
    # recipes.add_recipe('Earth', 'Fire', 'Iron')
    # recipes.add_recipe("Philosophers' stone", 'Iron', 'Silver')
    # recipes.add_recipe("Philosophers' stone", 'Silver', 'Gold')
    # recipes.add_recipe('Iron', 'Crystal', 'Talisman')
    # # ((Earth + Fire) + Philosophers' stone) + Philosophers' stone) = Gold
    # cauldron = Cauldron(recipes)
    # cauldron.add(Catalyst("Philosophers' stone", 2))
    # cauldron.add(AlchemicalElement('Fire'))
    # cauldron.get_content()
    # # Content:
    # #  * Fire x 1
    # #  * Philosophers' stone x 1
    #
    # cauldron.add(AlchemicalElement('Earth'))
    # print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Gold>]
    #
    # purifier = Purifier(recipes)
    # purifier.add(AlchemicalElement('Talisman'))
    # print(purifier.extract())  # -> [<AE: Earth>, <AE: Fire>, <AE: Crystal>]  (in any order)

    # philosophers_stone = Catalyst("Philosophers' stone", 2)
    #
    # recipes = AlchemicalRecipes()
    # recipes.add_recipe("Philosophers' stone", 'Mercury', 'Gold')
    # recipes.add_recipe("Fire", 'Earth', 'Iron')
    #
    # cauldron = Cauldron(recipes)
    # cauldron.add(philosophers_stone)
    # cauldron.add(AlchemicalElement('Mercury'))
    # print(cauldron.extract())  # -> [<C: Philosophers' stone (1)>, <AE: Gold>]
    #
    # cauldron.add(philosophers_stone)
    # cauldron.add(AlchemicalElement('Mercury'))
    # print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Gold>]
    #
    # cauldron.add(philosophers_stone)
    # cauldron.add(AlchemicalElement('Mercury'))
    # print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Mercury>]
    #
    # purifier = Purifier(recipes)
    # purifier.add(AlchemicalElement('Iron'))
    # print(purifier.extract())  # -> [<AE: Fire>, <AE: Earth>]    or      [<AE: Earth>, <AE: Fire>]

    # recipes = AlchemicalRecipes()
    # recipes.add_recipe("Water", "Fire", "Steam")
    # cauldron = Cauldron(recipes)
    # cauldron.add(AlchemicalElement("Water"))
    # cauldron.add(AlchemicalElement("Fire"))
    # try:
    #     # noinspection PyTypeChecker
    #     cauldron.add(69)
    # except TypeError:
    #     print("Raised TypeError correctly.")
    #
    # print(cauldron.elements)

    # recipes = AlchemicalRecipes()
    # recipes.add_recipe('Fire', 'Water', 'Steam')
    # recipes.add_recipe('Fire', 'Earth', 'Iron')
    # recipes.add_recipe('Water', 'Iron', 'Rust')
    #
    # print(recipes.recipe_book)
    #
    # print(recipes.get_product_name('Water', 'Fire'))  # -> 'Steam'
    #
    # try:
    #     recipes.add_recipe('Fire', 'Something else', 'Fire')
    #     print('Did not raise, not working as intended.')
    #
    # except DuplicateRecipeNamesException:
    #     print('Raised DuplicateRecipeNamesException, working as intended!')
    #
    # try:
    #     recipes.add_recipe('Fire', 'Earth', 'Gold')
    #     print('Did not raise, not working as intended.')
    #
    # except RecipeOverlapException:
    #     print('Raised RecipeOverlapException, working as intended!')
    #
    # cauldron = Cauldron(recipes)
    # cauldron.add(AlchemicalElement('Earth'))
    # cauldron.add(AlchemicalElement('Water'))
    # cauldron.add(AlchemicalElement('Fire'))
    #
    # print(cauldron.extract())  # -> [<AE: Earth>, <AE: Steam>]
    #
    # cauldron.add(AlchemicalElement('Earth'))
    # cauldron.add(AlchemicalElement('Earth'))
    # cauldron.add(AlchemicalElement('Earth'))
    # cauldron.add(AlchemicalElement('Fire'))
    # cauldron.add(AlchemicalElement('Fire'))
    # cauldron.add(AlchemicalElement('Water'))
    #
    # print(cauldron.extract())  # -> [<AE: Earth>, <AE: Iron>, <AE: Rust>]
    #
    # element_one = AlchemicalElement('Fire')
    # element_two = AlchemicalElement('Water')
    # element_three = AlchemicalElement('Water')
    # storage = AlchemicalStorage()
    #
    # print(element_one)  # <AE: Fire>
    # print(element_two)  # <AE: Water>
    #
    # storage.add(element_one)
    # storage.add(element_two)
    # print(storage.elements)
    # print(storage.get_content())
    # # Content:
    # #  * Fire x 1
    # #  * Water x 1
    # storage.add(AlchemicalElement("Water"))
    # storage.add(AlchemicalElement("Water"))
    # storage.add(AlchemicalElement("Water"))
    # storage.add(AlchemicalElement("Water"))
    # print(storage.get_content())
    # print(storage.extract())  # [<AE: Fire>, <AE: Water>]
    # print(storage.get_content())
    # # Content:
    # #  Empty
    #
    # storage.add(element_one)
    # storage.add(element_two)
    # storage.add(element_three)
    #
    # print(storage.pop('Water') == element_three)  # True
    # print(storage.pop('Water') == element_two)  # True
    #
    # storaage = AlchemicalStorage()
    # storaage.add(AlchemicalElement("Wind"))
    # storaage.add(AlchemicalElement("Fire"))
    # storaage.add(AlchemicalElement("Water"))
    # storaage.add(AlchemicalElement("Earth"))
    # print(storaage.get_content())
    #
    # print(storaage.elements)
