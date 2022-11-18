"""Tests if adventure.py game works correctly."""


import adventure as a


def test_adventurer_construction_and_representation():
    """Test if special cases are handled correctly."""
    assert a.Adventurer("Albert", "Druid", 3).__repr__() == "Albert, the Druid, Power: 3, Experience: 0."
    assert a.Adventurer("Steve", "Ungabunga", 100, -120).__repr__() == "Steve, the Fighter, Power: 10, Experience: 0."


def test_add_power():
    """Power addition function."""
    albert = a.Adventurer("Albert", "Druid", 3)
    albert.add_power(10)
    assert albert.power == 13
    albert.add_power(1304)
    assert albert.power == 1317


def test_add_experience():
    """Experience addition function."""
    albert = a.Adventurer("Albert", "Druid", 3)
    albert.add_experience(15)
    assert albert.experience == 15
    assert albert.power == 3
    albert.add_experience(314)
    assert albert.experience == 0
    assert albert.power == 35


def test_monster_class():
    """Test if Monster class functions correctly."""
    minecraft_zombie = a.Monster("Not a Creeper", "Zombie", 3_555_666)
    assert minecraft_zombie.name == "Undead Not a Creeper"
    assert minecraft_zombie.__repr__() == "Undead Not a Creeper of type Zombie, Power: 3555666."


def test_world_character_removal_and_reviving():
    """Character removing and graveyard reviving check."""
    world = a.World("King")

    peep = a.Adventurer("Peep", "Druid", 10, 10)
    toomas = a.Adventurer("Toomas", "Paladin", 20, 20)
    albert = a.Adventurer("Albert", "Wizard", 30, 30)
    joonas = a.Adventurer("Joonas", "xD", 40, 40)
    monster_joonas = a.Monster("Joonas", "Weirdo", 10)
    minecraft_zombie = a.Monster("Not a Creeper", "Zombie", 20)
    creeper = a.Monster("Creeper", "Creeper", 30)
    skeleton = a.Monster("Skeleton", "Skeleton", 40)
    enderman = a.Monster("Enderman", "Enderman", 10)

    world.add_adventurer(peep)
    world.add_adventurer(toomas)
    world.add_adventurer(albert)
    world.add_adventurer(joonas)
    world.add_adventurer(minecraft_zombie)

    world.add_monster(minecraft_zombie)
    world.add_monster(creeper)
    world.add_monster(albert)
    world.add_monster(skeleton)
    world.add_monster(enderman)
    world.add_monster(monster_joonas)

    assert world.master == "King" == world.get_python_master()
    assert world.get_adventurer_list() == [peep, toomas, albert, joonas]
    assert world.get_monster_list() == [minecraft_zombie, creeper, skeleton, enderman, monster_joonas]
    assert world.get_graveyard() == []
    world.remove_character("Albert")
    assert world.get_adventurer_list() == [peep, toomas, joonas]
    world.remove_character("Joonas")
    assert world.get_adventurer_list() == [peep, toomas]
    assert world.get_monster_list() == [minecraft_zombie, creeper, skeleton, enderman, monster_joonas]
    assert world.get_graveyard() == [albert, joonas]
    world.remove_character("Joonas")
    assert world.get_monster_list() == [minecraft_zombie, creeper, skeleton, enderman]
    assert world.get_graveyard() == [albert, joonas, monster_joonas]
    world.remove_character("Joonas")
    world.remove_character("Peep")
    assert world.get_graveyard() == [albert, monster_joonas, peep]
    world.necromancers_active(False)
    world.revive_graveyard()
    assert world.get_graveyard() == [albert, monster_joonas, peep]
    world.necromancers_active(True)
    world.revive_graveyard()
    assert world.get_graveyard() == []
    assert list(map(lambda x: x.__repr__(), world.monster_list)) == ["Undead Not a Creeper of type Zombie, Power: 20.",
                                                                     "Creeper of type Creeper, Power: 30.",
                                                                     "Skeleton of type Skeleton, Power: 40.",
                                                                     "Enderman of type Enderman, Power: 10.",
                                                                     "Undead Albert of type Zombie Wizard, Power: 30.",
                                                                     "Undead Joonas of type Zombie, Power: 10.",
                                                                     "Undead Peep of type Zombie Druid, Power: 10."]
    assert monster_joonas in world.monster_list
    world.remove_character("Joonas")
    assert world.get_graveyard() == []
    world.remove_character("Undead Joonas")
    assert world.get_graveyard() == [monster_joonas]
    world.revive_graveyard()
    assert world.get_graveyard() == [monster_joonas]


def test_making_adventurers_active():
    """Check if sorting and filtering functions function properly on adventurers."""
    other_world = a.World("Tiit")

    ab = a.Adventurer("ab", "gg", 1, 6)
    ac = a.Adventurer("ac", "gg", 2, 3)
    ad = a.Adventurer("ad", "gg", 1, 1)
    ae = a.Adventurer("ae", "gg", 6, 4)
    af = a.Adventurer("af", "gg", 5, 9)
    ag = a.Adventurer("ag", "gg", 3, 7)
    ah = a.Adventurer("ah", "gg", 8, 2)
    ai = a.Adventurer("ai", "gg", 3, 8)
    aj = a.Adventurer("aj", "gg", 9, 5)
    ak = a.Adventurer("ak", "Druid", 100, 100)
    al = a.Adventurer("al", "Druid", 0, 0)

    other_world.add_adventurer(ab)
    other_world.add_adventurer(ac)
    other_world.add_adventurer(ad)
    other_world.add_adventurer(ae)
    other_world.add_adventurer(af)
    other_world.add_adventurer(ag)
    other_world.add_adventurer(ah)
    other_world.add_adventurer(ai)
    other_world.add_adventurer(aj)
    other_world.add_adventurer(ak)
    other_world.add_adventurer(al)

    other_world.add_strongest_adventurer("Fighter")
    assert other_world.get_active_adventurers() == [aj]
    other_world.add_weakest_adventurer("Fighter")
    assert other_world.get_active_adventurers() == [ab, aj]
    other_world.add_most_experienced_adventurer("Fighter")
    assert other_world.get_active_adventurers() == [af, ab, aj]
    other_world.add_least_experienced_adventurer("Fighter")
    assert other_world.get_active_adventurers() == [af, ab, aj, ad]
    other_world.add_adventurer_by_name("ab")
    other_world.add_adventurer_by_name("ah")
    assert other_world.get_active_adventurers() == [af, ab, aj, ah, ad]
    other_world.add_least_experienced_adventurer("Fighter")
    assert other_world.get_active_adventurers() == [af, ab, aj, ac, ah, ad]
    other_world.add_all_adventurers_of_class_type("Druid")
    assert other_world.get_active_adventurers() == [ak, af, ab, aj, ac, ah, ad, al]
    other_world.add_all_adventurers()
    assert other_world.get_active_adventurers() == [ak, af, ai, ag, ab, aj, ae, ac, ah, ad, al]


def test_making_monsters_active():
    """Check if sorting and filtering functions function properly on monsters."""
    other_world = a.World("Sukk")

    mb = a.Monster("mb", "Goblin", 0)
    mc = a.Monster("mc", "Goblin", 2)
    md = a.Monster("md", "Goblin", 4)
    me = a.Monster("me", "Goblin", 6)
    mf = a.Monster("mf", "Goblin", 5)
    mg = a.Monster("mg", "Goblin", 7)
    mh = a.Monster("mh", "Goblin", 8)
    mi = a.Monster("mi", "Goblin", 3)
    mj = a.Monster("mj", "Goblin", 100)
    mk = a.Monster("mk", "Troll", 1)
    ml = a.Monster("ml", "Troll", 9)

    other_world.add_monster(mb)
    other_world.add_monster(mc)
    other_world.add_monster(md)
    other_world.add_monster(me)
    other_world.add_monster(mf)
    other_world.add_monster(mg)
    other_world.add_monster(mh)
    other_world.add_monster(mi)
    other_world.add_monster(mj)
    other_world.add_monster(mk)
    other_world.add_monster(ml)

    other_world.add_strongest_monster()
    assert other_world.get_active_monsters() == [mj]
    other_world.add_weakest_monster()
    assert other_world.get_active_monsters() == [mj, mb]
    other_world.add_monster_by_name("mc")
    other_world.add_monster_by_name("md")
    assert other_world.get_active_monsters() == [mj, md, mc, mb]
    other_world.add_all_monsters_of_type("Troll")
    assert other_world.get_active_monsters() == [mj, ml, md, mc, mk, mb]
    other_world.add_all_monsters()
    assert other_world.get_active_monsters() == [mj, ml, mh, mg, me, mf, md, mi, mc, mk, mb]


def test_battle_behaviour_deadly_lose__no_zombies__no_animals():
    """Go adventure, deadly, adventurers lose, there are no zombies and there are no animals."""
    world = a.World("King")

    peep = a.Adventurer("Peep", "Druid", 10, 10)
    toomas = a.Adventurer("Toomas", "Paladin", 20, 20)
    albert = a.Adventurer("Albert", "Wizard", 30, 30)
    joonas = a.Adventurer("Joonas", "xD", 40, 80)
    monster_joonas = a.Monster("Joonas", "Weirdo", 10)
    minecraft_troll = a.Monster("Not a Creeper", "Troll", 21)
    creeper = a.Monster("Creeper", "Creeper", 30)
    skeleton = a.Monster("Skeleton", "Skeleton", 40)
    enderman = a.Monster("Enderman", "Enderman", 10)

    world.add_adventurer(peep)
    world.add_adventurer(toomas)
    world.add_adventurer(albert)
    world.add_adventurer(joonas)

    world.add_monster(minecraft_troll)
    world.add_monster(creeper)
    world.add_monster(skeleton)
    world.add_monster(enderman)
    world.add_monster(monster_joonas)

    world.add_all_adventurers()
    world.add_all_monsters()
    world.go_adventure(True)

    assert world.get_active_adventurers() == []
    assert world.get_active_monsters() == []
    assert world.get_adventurer_list() == []
    assert world.get_monster_list() == [minecraft_troll, creeper, skeleton, enderman, monster_joonas]
    assert world.get_graveyard() == [peep, toomas, albert, joonas]


def test_battle_behaviour_deadly_win__zombies__no_animals():
    """Go adventure, deadly, adventurers win, there are zombies, but there are no animals."""
    world = a.World("King")

    peep = a.Adventurer("Peep", "Druid", 10, 10)
    toomas = a.Adventurer("Toomas", "Paladin", 20, 20)
    albert = a.Adventurer("Albert", "Wizard", 30, 30)
    joonas = a.Adventurer("Joonas", "xD", 40, 80)
    monster_joonas = a.Monster("Joonas", "Weirdo", 10)
    minecraft_zombie = a.Monster("Not a Creeper", "Zombie", 21)
    creeper = a.Monster("Creeper", "Creeper", 30)
    skeleton = a.Monster("Skeleton", "Skeleton", 40)
    enderman = a.Monster("Enderman", "Enderman", 10)

    world.add_adventurer(peep)
    world.add_adventurer(toomas)
    world.add_adventurer(albert)
    world.add_adventurer(joonas)

    world.add_monster(minecraft_zombie)
    world.add_monster(creeper)
    world.add_monster(skeleton)
    world.add_monster(enderman)
    world.add_monster(monster_joonas)

    world.add_all_adventurers()
    world.add_all_monsters()
    world.go_adventure(True)

    assert world.get_active_adventurers() == []
    assert world.get_active_monsters() == []
    assert world.get_adventurer_list() == [peep, toomas, albert, joonas]
    assert world.get_monster_list() == []
    assert world.get_graveyard() == [minecraft_zombie, creeper, skeleton, enderman, monster_joonas]
    assert peep.experience == 64
    assert toomas.experience == 74
    assert toomas.power == 20
    assert albert.experience == 84
    assert joonas.experience == 0
    assert joonas.power == 53

    # At this point, 90% coverage was reached.


def test_battle_behaviour_deadly_win__no_zombies__animals():
    """Go adventure, deadly, adventurers win, there are no zombies, but there are animals."""
    world = a.World("King")

    peep = a.Adventurer("Peep", "Druid", 10, 10)
    toomas = a.Adventurer("Toomas", "Paladin", 20, 20)
    albert = a.Adventurer("Albert", "Wizard", 30, 30)
    joonas = a.Adventurer("Joonas", "xD", 40, 80)
    monster_joonas = a.Monster("Joonas", "Weirdo", 10)
    minecraft_pig = a.Monster("Not a Creeper", "Animal", 21)
    creeper = a.Monster("Creeper", "Creeper", 30)
    skeleton = a.Monster("Skeleton", "Skeleton", 40)
    enderman = a.Monster("Enderman", "Enderman", 10)

    world.add_adventurer(peep)
    world.add_adventurer(toomas)
    world.add_adventurer(albert)
    world.add_adventurer(joonas)

    world.add_monster(minecraft_pig)
    world.add_monster(creeper)
    world.add_monster(skeleton)
    world.add_monster(enderman)
    world.add_monster(monster_joonas)

    world.add_all_adventurers()
    world.add_all_monsters()
    world.go_adventure(True)

    assert world.get_active_adventurers() == []
    assert world.get_active_monsters() == []
    assert world.get_adventurer_list() == [peep, toomas, albert, joonas]
    assert world.get_monster_list() == [minecraft_pig]
    assert world.get_graveyard() == [creeper, skeleton, enderman, monster_joonas]


def test_battle_behaviour_not_deadly_win__zombies__no_animals():
    """Go adventure, not deadly, adventurers win, there are zombies, but there are no animals."""
    world = a.World("King")

    peep = a.Adventurer("Peep", "Druid", 10, 10)
    toomas = a.Adventurer("Toomas", "Paladin", 20, 20)
    albert = a.Adventurer("Albert", "Wizard", 30, 30)
    joonas = a.Adventurer("Joonas", "xD", 40, 80)
    monster_joonas = a.Monster("Joonas", "Weirdo", 10)
    minecraft_zombie = a.Monster("Not a Creeper", "Zombie", 21)
    creeper = a.Monster("Creeper", "Creeper", 30)
    skeleton = a.Monster("Skeleton", "Skeleton", 40)
    enderman = a.Monster("Enderman", "Enderman", 10)

    world.add_adventurer(peep)
    world.add_adventurer(toomas)
    world.add_adventurer(albert)
    world.add_adventurer(joonas)

    world.add_monster(minecraft_zombie)
    world.add_monster(creeper)
    world.add_monster(skeleton)
    world.add_monster(enderman)
    world.add_monster(monster_joonas)

    world.add_all_adventurers()
    world.add_all_monsters()
    world.go_adventure(False)

    assert world.get_active_adventurers() == []
    assert world.get_active_monsters() == []
    assert world.get_adventurer_list() == [peep, toomas, albert, joonas]
    assert world.get_monster_list() == [minecraft_zombie, creeper, skeleton, enderman, monster_joonas]
    assert world.get_graveyard() == []
    assert peep.experience == 37
    assert toomas.experience == 47
    assert toomas.power == 20
    assert albert.experience == 57
    assert joonas.experience == 0


def test_battle_behaviour_not_deadly_lose__zombies__no_animals():
    """Go adventure, not deadly, adventurers lose, there are zombies, but there are no animals."""
    world = a.World("King")

    peep = a.Adventurer("Peep", "Druid", 10, 10)
    toomas = a.Adventurer("Toomas", "Paladin", 10, 20)
    albert = a.Adventurer("Albert", "Wizard", 30, 30)
    joonas = a.Adventurer("Joonas", "xD", 40, 80)
    monster_joonas = a.Monster("Joonas", "Weirdo", 10)
    minecraft_zombie = a.Monster("Not a Creeper", "Zombie", 21)
    creeper = a.Monster("Creeper", "Creeper", 30)
    skeleton = a.Monster("Skeleton", "Skeleton", 40)
    enderman = a.Monster("Enderman", "Enderman", 10)

    world.add_adventurer(peep)
    world.add_adventurer(toomas)
    world.add_adventurer(albert)
    world.add_adventurer(joonas)

    world.add_monster(minecraft_zombie)
    world.add_monster(creeper)
    world.add_monster(skeleton)
    world.add_monster(enderman)
    world.add_monster(monster_joonas)

    world.add_all_adventurers()
    world.add_all_monsters()
    world.go_adventure(False)

    assert world.get_active_adventurers() == []
    assert world.get_active_monsters() == []
    assert world.get_adventurer_list() == [peep, toomas, albert, joonas]
    assert world.get_monster_list() == [minecraft_zombie, creeper, skeleton, enderman, monster_joonas]
    assert world.get_graveyard() == []
    assert peep.experience == 10
    assert toomas.experience == 20
    assert toomas.power == 10
    assert albert.experience == 30
    assert joonas.experience == 80


def test_battle_behaviour_deadly_tie__zombies__no_animals():
    """Go adventure, deadly, tie, there are zombies, but there are no animals."""
    world = a.World("King")

    peep = a.Adventurer("Peep", "Druid", 10, 10)
    toomas = a.Adventurer("Toomas", "Paladin", 10, 20)
    albert = a.Adventurer("Albert", "Wizard", 30, 30)
    joonas = a.Adventurer("Joonas", "xD", 40, 80)
    monster_joonas = a.Monster("Joonas", "Weirdo", 10)
    minecraft_zombie = a.Monster("Not a Creeper", "Zombie", 10)
    creeper = a.Monster("Creeper", "Creeper", 30)
    skeleton = a.Monster("Skeleton", "Skeleton", 40)
    enderman = a.Monster("Enderman", "Enderman", 10)

    world.add_adventurer(peep)
    world.add_adventurer(toomas)
    world.add_adventurer(albert)
    world.add_adventurer(joonas)

    world.add_monster(minecraft_zombie)
    world.add_monster(creeper)
    world.add_monster(skeleton)
    world.add_monster(enderman)
    world.add_monster(monster_joonas)

    world.add_all_adventurers()
    world.add_all_monsters()
    world.go_adventure(False)

    assert world.get_active_adventurers() == []
    assert world.get_active_monsters() == []
    assert world.get_adventurer_list() == [peep, toomas, albert, joonas]
    assert world.get_monster_list() == [minecraft_zombie, creeper, skeleton, enderman, monster_joonas]
    assert world.get_graveyard() == []
    assert peep.experience == 22
    assert toomas.experience == 32
    assert toomas.power == 10
    assert albert.experience == 42
    assert joonas.experience == 92
