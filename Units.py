# This file defines and represents what a unit is

class Unit:
    """ The Definition of A unit """

    # things that make up a unit
    player = ["Class"]
    player.health = 20.0
    player.sanity = 10.0
    player.name = name
    player.ability = [6]

    def __init__(self, health, sanity):
        self.health = health
        self.sanity = sanity

    def __int__(self, stats):
        self.Acc = 0
        self.Crit = 0
        self.DMG = 0
        self.Dodge = 0
        self.Prot = 0
        self.Spd =0

    def command(self, turn):
        if turn == self.name:
            self.attack(1)
        elif turn == self.name:
            self.attack(2)
        elif turn == self.name:
            self.attack(3)
        elif turn == self.name:
            self.attack(4)
        elif turn == self.name: # this option represents changing places with another ally
            self.attack(5)
        else:
            self.name: "cancel"

    def movment(self):
        for i in range(hallway):
            print("working")


class Unit():
    GraveRobber = unit()
    GraveRobber.health = 20.0
    GraveRobber.sanity = 10.0
    GraveRobber.name = wilma
    GraveRobber.ability = [6]

