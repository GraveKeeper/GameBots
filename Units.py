# This file defines and represents what a unit is
from binarytree import build

class Unittype:
    """ The Definition of A unit """
    # 18 type objects with unique values
    # things that make up a unit
    # needs a retraval function for every type of information used by a character
    player = ["Class"]
    """
    player.health = 20.0
    player.sanity = 10.0
    player.name = name
    player.ability = [6]
    """
    # information for all characters
    def __init__(self, health, sanity):
        self.health = health
        self.sanity = sanity

    # character attributes
    def __int__(self, accuracy, critical, damage, dodge, protect, speed):
        self.accuracy = get.accuracy
        self.critical = get.critical
        self.damage = get.damage
        self.dodge = get.dodge
        self.protect = get.protect
        self.speed = get.speed

    def command(self, turn):
        pass
        # array for all ability that can be used
        # there are 144 unique


class Character:
    # need to receive data from unit type class
    # take name of characters from screen
    def __init__(self, name, type):
        self.name = get.name
        self.type = get.type
    # take inital actions
    # put in array that can change over time depending on what abilitys it knows or learns
    names = [2]
    names.append(self.name)
    # pointer to unit type object to use get functions
    # also needs to grab the abilitys in use an array of 4

# redundant
class test:
    # binary tree of unit types needs to search for the type it wants to referance abilitys
    # List of nodes
    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17]
    # Building the binary tree
    binary_tree = build(nodes)
    print('Binary tree from list :\n',
          binary_tree)
    print('\nList from binary tree :',
          binary_tree.values)
    # also can use sorted array
    # create


class party:
    pass
    # controls the party movement and interactions
