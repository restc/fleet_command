import pygame
import sys

class Ship:

    kind = "ship"
    hullHealth = 100

    def __init__(self, kind):
        self.kind = kind

    def healHull(amountHealed):
        if hullHealth + amountHealed > 100:
            hullHealth = 100
        else:
            hullHealth = hullHealth + amountHealed

    def damageHull(self, damage):
        hullHealth = hullHealth - damage
        if hullHealth < 1:
            return ship_sunk
        else:
            return hullHealth


    def ship_sunk():
        return self.kind + " has been eliminated."


s = Ship("Battleship")
print "Kind: {0}".format(s.kind)
print "Hull Health: {0}".format(s.hullHealth)
s.damageHull(20)
print "Hull Health: {0}".format(s.hullHealth)
