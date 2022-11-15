"""$0.10 game from Walmart."""


class Adventurer:
    """Class that holds the player data."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Class constructor."""
        self.name = name
        if class_type not in ["Druid", "Wizard", "Paladin"]:
            self.class_type = "Fighter"
        else:
            self.class_type = class_type
        if power > 99:
            self.power = 10
        else:
            self.power = power
        if experience > 0:
            self.experience = experience
        else:
            self.experience = 0

    def add_power(self, power: int):
        """Increase the power stat."""
        if power > 0:
            self.power += power

    def add_experience(self, exp: int):
        """Increase the experience stat. If experience is 100 or more, increase power instead."""
        if exp > 0:
            self.experience += exp
        if self.experience > 99:
            self.power += self.experience // 10
            self.experience = 0

    def __repr__(self):
        """Class representation."""
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."


class Monster:
    """Enemies of the Adventurer."""

    def __init__(self, name: str, type: str, power: int):
        """Class constructor."""
        self.type = type
        self.power = power
        if self.type == "Zombie":
            self.name = "Undead " + name
        else:
            self.name = name

    def __repr__(self):
        """Class representation."""
        return f"{self.name} of type {self.type}, Power: {self.power}."


class World:
    """Stores Adventurers, Monsters and holds the game functions."""

    def __init__(self, master):
        self.master = master
        self.adventurer_list = []
        self.monster_list = []
        self.graveyard = []

    def get_python_master(self):
        """Return the python master."""
        return self.master

    def get_monster_list(self):
        """Return the monster list."""
        return self.monster_list

    def get_adventurer_list(self):
        """Return the adventurer list."""
        return self.adventurer_list

    def get_graveyard(self):
        """Return the graveyard list."""
        return self.graveyard

    def add_adventurer(self, adventurer: Adventurer):
        """Add adventurer to the list."""
        if type(adventurer) is Adventurer:
            self.adventurer_list.append(adventurer)

    def add_monster(self, monster: Monster):
        """Add monster to the list."""
        if type(monster) is Monster:
            self.monster_list.append(monster)


if __name__ == "__main__":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    friend.add_power(20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

    world.add_monster(annoying_friend)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    world.add_adventurer(annoying_friend)
    print()

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)

    print()
    print("Mängime esimese seikluse läbi!")
    world.add_strongest_adventurer("Druid")
    world.add_strongest_monster()
    print(world.get_active_adventurers())  # -> Peep
    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print(
        "Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")