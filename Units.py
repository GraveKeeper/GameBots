# This file defines and represents what a unit is
# from binarytree import build
# global list of all character/unit types
CharacterList = ('Abomination', 'Antiquarian', 'Arbalest', 'Bark', 'Bounty Hunter',
                 'Crusader', 'Flagellant', 'Grave Robber', 'Hellion', 'Highwayman', 'Houndmaster',
                 'Jester', 'Leper', 'Man-at-Arms', 'Musketeer', 'Occultist', 'Plague Doctor',
                 'Shieldbreaker', 'Vestal')


class Unit(object):
    """ The Definition of A unit """

    # 18 type objects with unique values
    # things that make up a unit
    # needs a retrieval function for every type of information used by a character

    # character attributes
    def __init__(self, accuracy, critical, damage, dodge, protect, speed, health, sanity):
        self.accuracy = accuracy
        self.critical = critical
        self.damage = damage
        self.dodge = dodge
        self.protect = protect
        self.speed = speed
        self.health = health
        self.sanity = sanity

    # array for all ability that can be used
    def abilities(self, turn):
        self.turn = turn(1, 2, 3, 4, 5, 6)
        # there are 144 unique ability's


# subclass of unit that should be able to grab a unit type
class UnitType(Unit):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        super().__init__(name, type)


class Party:
    pass
    # controls the party movement and interactions

# things I probably don't need
# class Character:
# need to receive data from unit type class
# take name of characters from screen
# take initial actions
# put in array that can change over time depending on what ability's it knows or learns
# names = [2]
# names.append(self.name)
# pointer to unit type object to use get functions
# also needs to grab the ability's in use an array of 4
