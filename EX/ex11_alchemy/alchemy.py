"""Alchemy."""


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.elements = []

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError
        exception.

        :param element: Input object to add to storage.
        """
        if type(element) is AlchemicalElement:
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
            if f"{first_component_name} + {second_component_name}" in recipe or \
                    f"{second_component_name} + {first_component_name}" in recipe:
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

    def add(self, element: AlchemicalElement):
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
        super().add(element)
        for recipe in self.recipes.recipe_book:
            for item in self.elements:
                for item2 in self.elements:
                    if f"{item.name} + {item2.name}" in recipe:
                        self.elements.remove(item)
                        self.elements.remove(item2)
                        self.elements.append(AlchemicalElement(recipe.split("= ")[-1]))
                        break


if __name__ == '__main__':
    recipes = AlchemicalRecipes()
    recipes.add_recipe('Fire', 'Water', 'Steam')
    recipes.add_recipe('Fire', 'Earth', 'Iron')
    recipes.add_recipe('Water', 'Iron', 'Rust')

    print(recipes.recipe_book)

    print(recipes.get_product_name('Water', 'Fire'))  # -> 'Steam'

    try:
        recipes.add_recipe('Fire', 'Something else', 'Fire')
        print('Did not raise, not working as intended.')

    except DuplicateRecipeNamesException:
        print('Raised DuplicateRecipeNamesException, working as intended!')

    try:
        recipes.add_recipe('Fire', 'Earth', 'Gold')
        print('Did not raise, not working as intended.')

    except RecipeOverlapException:
        print('Raised RecipeOverlapException, working as intended!')

    cauldron = Cauldron(recipes)
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Water'))
    cauldron.add(AlchemicalElement('Fire'))

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Steam>]

    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Water'))

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Iron>, <AE: Rust>]

    element_one = AlchemicalElement('Fire')
    element_two = AlchemicalElement('Water')
    element_three = AlchemicalElement('Water')
    storage = AlchemicalStorage()

    print(element_one)  # <AE: Fire>
    print(element_two)  # <AE: Water>

    storage.add(element_one)
    storage.add(element_two)
    print(storage.elements)
    print(storage.get_content())
    # Content:
    #  * Fire x 1
    #  * Water x 1
    storage.add(AlchemicalElement("Water"))
    storage.add(AlchemicalElement("Water"))
    storage.add(AlchemicalElement("Water"))
    storage.add(AlchemicalElement("Water"))
    print(storage.get_content())
    print(storage.extract())  # [<AE: Fire>, <AE: Water>]
    print(storage.get_content())
    # Content:
    #  Empty

    storage.add(element_one)
    storage.add(element_two)
    storage.add(element_three)

    print(storage.pop('Water') == element_three)  # True
    print(storage.pop('Water') == element_two)  # True

    storaage = AlchemicalStorage()
    storaage.add(AlchemicalElement("Wind"))
    storaage.add(AlchemicalElement("Fire"))
    storaage.add(AlchemicalElement("Water"))
    storaage.add(AlchemicalElement("Earth"))
    print(storaage.get_content())

    print(storaage.elements)
