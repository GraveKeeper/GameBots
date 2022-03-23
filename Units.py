# This file defines and represents what a unit is

# Unit stats
def units():
    health = 0
    abilitys = 0
    sanity = 0


# shows what a unit can do in combat
def unit_turn():
    attack1 = 0
    attack2 = 0
    attack3 = 0
    attack4 = 0


class Unit:
    """ The Definition of A unit """

    # things that make up a unit
    player = ["Class"]

    def __init__(self, health, sanity):
        self.health = health
        self.sanity = sanity


    def command(self, turn):
        if turn == self.name
            self.attack(1)
        elif turn == self.health