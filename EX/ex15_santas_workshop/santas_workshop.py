"""Merry Christmas!"""

import requests
import csv


class Child:
    """Data about a child."""

    def __init__(self, name: str, naughty: bool, country: str, wishes: list):
        """Class constructor."""
        self.name = name
        self.naughty = naughty
        self.country = country
        self.wishes = wishes

    def __repr__(self):
        """Class representation."""
        return self.name


class Gift:
    """Data about a gift."""

    def __init__(self, name: str, material_cost: int, production_time: int, weight_in_grams: int):
        """
        Initialize a new instance of the class with the given name, material cost, production time,
        and weight in grams.
        """
        self.name = name
        self.material_cost = material_cost
        self.production_time = production_time
        self.weight_in_grams = weight_in_grams

    def __repr__(self):
        """Class representation."""
        return self.name


def get_list_of_children(nice_file: str, naughty_file: str, wish_file: str):
    """Makes a list of children."""
    children = []
    nice_dict = {}
    naughty_dict = {}
    wish_dict = {}

    with open(nice_file) as nice:
        nice_children = nice.read().split("\n")
    with open(naughty_file) as naughty:
        naughty_children = naughty.read().splitlines()
    with open(wish_file) as wish:
        wishes = wish.read().splitlines()

    for child in nice_children:
        nice_dict[child.split(", ")[0]] = child.split(", ")[1]
    for child in naughty_children:
        naughty_dict[child.split(", ")[0]] = child.split(", ")[1]
    for child in wishes:
        wish_dict[child.split(", ")[0]] = child.split(", ")[1:]

    for child in nice_dict:
        wish_list = []
        if child in wish_dict:
            for w in wish_dict[child]:
                url = w.replace(" ", "%20")
                present = requests.get(f"https://cs.ttu.ee/services/xmas/gift?name={url}").json()
                wish_list.append(Gift(w, int(present["material_cost"]), int(present["production_time"]),
                                      int(present["weight_in_grams"])))
        children.append(Child(child, False, nice_dict[child], wish_list))

    for child in naughty_dict:
        wish_list = [Gift("Coal", 1, 0, 100)]
        children.append(Child(child, True, naughty_dict[child], wish_list))

    return children


if __name__ == '__main__':
    list_of_children = [
        Child("Joonas", False, "Estonia", [
            Gift('Wall-mount diamond pickaxe', 15, 1, 8200),
            Gift('Mermaid barbie', 15, 1, 5000),
            Gift('Pink fluffy pen', 15, 1, 6000)
        ]),
        Child("Toomas", False, "Estonia", [
            Gift('LED light up sneakers', 15, 1, 12000),
            Gift('Toy train set', 15, 1, 8000),
            Gift('Book about dinosaurs', 15, 1, 9000)
        ]),
        Child("Albert", False, "Estonia", [
            Gift('Dungeons and Dragons 5th Edition Starter Set', 15, 1, 5000),
            Gift('Book about dinosaurs', 15, 1, 5000),
            Gift('Wall-mount diamond pickaxe', 15, 1, 5000)
        ]),
        Child("Martha", False, "United Kingdom", [
            Gift('Mermaid barbie', 15, 1, 125),
            Gift('Wall-mount diamond pickaxe', 15, 1, 123),
            Gift('LED light up sneakers', 15, 1, 912)
        ]),
        Child("Eliza", False, "United Kingdom", [
            Gift('Briefcase of art supplies', 15, 1, 122),
            Gift('Toy train set', 15, 1, 1275),
            Gift('Mermaid barbie', 15, 1, 125)
        ]),
        Child("Donald", False, "United States of America", [
            Gift('Briefcase of art supplies', 15, 1, 126),
            Gift('LED light up sneakers', 15, 1, 128),
            Gift('Wall-mount diamond pickaxe', 15, 1, 192)
        ]),
        Child("Joe", False, "United States of America", [
            Gift('Book about dinosaurs', 15, 1, 1072),
            Gift('Toy train set', 15, 1, 127),
            Gift('Wall-mount diamond pickaxe', 15, 1, 1253)
        ]),
    ]



