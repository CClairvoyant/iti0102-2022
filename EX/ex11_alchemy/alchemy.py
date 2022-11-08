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


if __name__ == '__main__':
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
    storaage = AlchemicalStorage()
    storaage.add(AlchemicalElement("Wind"))
    storaage.add(AlchemicalElement("Fire"))
    storaage.add(AlchemicalElement("Water"))
    storaage.add(AlchemicalElement("Earth"))
    print(storaage.get_content())
