import pygame
import sys

class Ship:

    def __init__(self, kind):
        self.kind = kind
        self.hullHealth = 100

    def healHull(self, heal):
        if hullHealth + heal > 100:
            hullHealth = 100
        else:
            hullHealth = hullHealth + heal

    def damageHull(self, damage):
        hullHealth = hullHealth - damage
        if hullHealth < 1:
            return ship_sunk
        else:
            return hullHealth

    def ship_sunk(self):
        return self.kind + " has been eliminated."

    def canMove(self):
        False

    def info(self):
        print "Kind: {0}".format(self.kind)
        print "Hull Health: {0}".format(self.hullHealth)


class Weapon:

    def __init__(self, kind):
        self.kind = kind

    def damage(self, amount):
        self.damage = damage


s = Ship("Battleship")
print "Kind: {0}".format(s.kind)
print "Hull Health: {0}".format(s.hullHealth)
s.damageHull(20)
print "Hull Health: {0}".format(s.hullHealth)
