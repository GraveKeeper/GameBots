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

    def __init__(self, health, sanity):
        self.health = health
        self.sanity = sanity

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



class character:
    pass
    # need to receive data from unit type class
    # take name
    # take inital actions
    # put in array that can change over time depending on what abilitys it knows or learns
    # pointer to unit type object to use get functions
    # also needs to grab the abilitys in use an array of 4

# redundant
class test:
    # binary tree of unit types needs to search for the type it wants to referance abilitys
    # List of nodes
    nodes = [3, 6, 8, 2, 11, None, 13]
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
