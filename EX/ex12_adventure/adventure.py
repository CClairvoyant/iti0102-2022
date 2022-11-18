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
        self.__name = name

    @property
    def name(self):
        if self.type == "Zombie":
            return "Undead " + self.__name
        else:
            return self.__name

    def __repr__(self):
        """Class representation."""
        return f"{self.name} of type {self.type}, Power: {self.power}."


class World:
    """Stores Adventurers, Monsters and holds the game functions."""

    def __init__(self, master):
        """Class constructor."""
        self.master = master
        self.adventurer_list = []
        self.active_adventurer_list = []
        self.monster_list = []
        self.active_monster_list = []
        self.graveyard = []
        self.necromancers = False

    def get_python_master(self):
        """Return the python master."""
        return self.master

    def get_monster_list(self):
        """Return the monster list."""
        return list(filter(lambda x: x not in self.active_monster_list, self.monster_list))

    def get_adventurer_list(self):
        """Return the adventurer list."""
        return list(filter(lambda x: x not in self.active_adventurer_list, self.adventurer_list))

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

    def remove_character(self, name: str):
        """Remove ONE character from a list with a priority of Adventurer > Monster > Graveyard."""
        adv_names_list = list(map(lambda x: x.name, self.adventurer_list))
        mon_names_list = list(map(lambda x: x.name, self.monster_list))
        grave_names_list = list(map(lambda x: x.name, self.graveyard))
        if name in adv_names_list:
            self.graveyard.append(self.adventurer_list.pop(adv_names_list.index(name)))
        elif name in mon_names_list:
            self.graveyard.append(self.monster_list.pop(mon_names_list.index(name)))
        elif name in grave_names_list:
            self.graveyard.pop(grave_names_list.index(name))

    def necromancers_active(self, active: bool):
        """Change the necromancer existence status."""
        self.necromancers = active

    def revive_graveyard(self):
        """Revive all dead characters if necromancers exist."""
        if self.necromancers:
            for dead in self.graveyard:
                if type(dead) is Monster:
                    dead.type = "Zombie"
                    self.monster_list.append(dead)
                elif type(dead) is Adventurer:
                    self.monster_list.append(Monster("Undead " + dead.name, "Zombie " + dead.class_type, dead.power))
            self.graveyard = []
            self.necromancers = False

    def get_active_adventurers(self):
        """Return all active adventurers, sorted by experience descending."""
        return sorted(self.active_adventurer_list, key=lambda x: -x.experience)

    def add_strongest_adventurer(self, class_type: str):
        """Make the strongest adventurer active."""
        self.active_adventurer_list.append(list(filter(lambda x: x.class_type == class_type and x not in self.active_adventurer_list, sorted(self.adventurer_list, key=lambda x: -x.power)))[0])

    def add_weakest_adventurer(self, class_type: str):
        """Make the weakest adventurer active."""
        self.active_adventurer_list.append(list(filter(lambda x: x.class_type == class_type and x not in self.active_adventurer_list, sorted(self.adventurer_list, key=lambda x: x.power)))[0])

    def add_most_experienced_adventurer(self, class_type: str):
        """Make the most experienced adventurer active."""
        self.active_adventurer_list.append(list(filter(lambda x: x.class_type == class_type and x not in self.active_adventurer_list, sorted(self.adventurer_list, key=lambda x: -x.experience)))[0])

    def add_least_experienced_adventurer(self, class_type: str):
        """Make the least experienced adventurer active."""
        self.active_adventurer_list.append(list(filter(lambda x: x.class_type == class_type and x not in self.active_adventurer_list, sorted(self.adventurer_list, key=lambda x: x.experience)))[0])

    def add_adventurer_by_name(self, name: str):
        """Make the adventurer with the given name active."""
        self.active_adventurer_list += filter(lambda x: x.name == name and x not in self.active_adventurer_list, self.adventurer_list)

    def add_all_adventurers_of_class_type(self, class_type: str):
        """Make all the adventurers with the given class type active."""
        self.active_adventurer_list += filter(lambda x: x.class_type == class_type and x not in self.active_adventurer_list, self.adventurer_list)

    def add_all_adventurers(self):
        """Make all the adventurers active."""
        self.active_adventurer_list += filter(lambda x: x not in self.active_adventurer_list, self.adventurer_list)

    def get_active_monsters(self):
        """Return active monsters."""
        return sorted(self.active_monster_list, key=lambda x: -x.power)

    def add_monster_by_name(self, name: str):
        """Make the monsters with the given name active."""
        self.active_monster_list += filter(lambda x: x not in self.active_monster_list and x.name == name, self.monster_list)

    def add_strongest_monster(self):
        """Make the strongest monster active."""
        self.active_monster_list.append(sorted(list(filter(lambda x: x not in self.active_monster_list, self.monster_list)), key=lambda x: -x.power)[0])

    def add_weakest_monster(self):
        """Make the weakest monster active."""
        self.active_monster_list.append(sorted(list(filter(lambda x: x not in self.active_monster_list, self.monster_list)), key=lambda x: x.power)[0])

    def add_all_monsters_of_type(self, type: str):
        """Make all the monsters with the given type active."""
        self.active_monster_list += filter(lambda x: x not in self.active_monster_list and x.type == type, self.monster_list)

    def add_all_monsters(self):
        """Make all the monsters active."""
        self.active_monster_list += filter(lambda x: x not in self.active_monster_list, self.monster_list)

    def go_adventure(self, deadly: bool = False):
        """Battle rules and functions."""
        zombies_in_game = False
        if list(filter(lambda x: x.class_type == "Druid", self.active_adventurer_list)):
            self.active_monster_list = list(filter(lambda x: x.type not in ["Animal", "Ent"], self.active_monster_list))
        if list(filter(lambda x: "Zombie" in x.type, self.active_monster_list)):
            for paladin in list(filter(lambda x: x.class_type == "Paladin", self.active_adventurer_list)):
                paladin.power = paladin.power * 2
            zombies_in_game = True
        gained_xp = sum(list(map(lambda x: x.power, self.active_monster_list))) // len(self.active_adventurer_list)
        if sum(list(map(lambda x: x.power, self.active_adventurer_list))) > sum(list(map(lambda x: x.power, self.active_monster_list))):
            self.adventurers_win(deadly, gained_xp, zombies_in_game)
        elif sum(list(map(lambda x: x.power, self.active_adventurer_list))) < sum(list(map(lambda x: x.power, self.active_monster_list))):
            self.monsters_win(deadly, zombies_in_game)
        else:
            if zombies_in_game:
                for paladin in list(filter(lambda x: x.class_type == "Paladin", self.active_adventurer_list)):
                    paladin.power = paladin.power // 2
            for adventurer in self.active_adventurer_list:
                adventurer.add_experience(gained_xp // 2)
            self.active_adventurer_list.clear()
            self.active_monster_list.clear()

    def monsters_win(self, deadly, zombies_in_game):
        """Execute if the monsters win the battle."""
        if zombies_in_game:
            for paladin in list(filter(lambda x: x.class_type == "Paladin", self.active_adventurer_list)):
                paladin.power = paladin.power // 2
        if deadly:
            self.active_monster_list.clear()
            self.adventurer_list = list(filter(lambda x: x not in self.active_adventurer_list, self.adventurer_list))
            self.graveyard += self.active_adventurer_list
            self.active_adventurer_list.clear()
        else:
            self.active_adventurer_list.clear()
            self.active_monster_list.clear()

    def adventurers_win(self, deadly, gained_xp, zombies_in_game):
        """Execute if the adventurers win the battle."""
        if zombies_in_game:
            for paladin in list(filter(lambda x: x.class_type == "Paladin", self.active_adventurer_list)):
                paladin.power = paladin.power // 2
        if deadly:
            for adventurer in self.active_adventurer_list:
                adventurer.add_experience(gained_xp * 2)
            self.active_adventurer_list.clear()
            self.monster_list = list(filter(lambda x: x not in self.active_monster_list, self.monster_list))
            self.graveyard += self.active_monster_list
            self.active_monster_list.clear()
        else:
            for adventurer in self.active_adventurer_list:
                adventurer.add_experience(gained_xp)
            self.active_adventurer_list.clear()
            self.active_monster_list.clear()

