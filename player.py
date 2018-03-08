import pygame
from enum import Enum

class Player:

    def __init__(self, sprite, orient):
        self.health = 10
        self.sprite = sprite
        self.orientation = orient
        self.guarding = False
        self.atking = False
        self.damaged = False
        self.flicker = 0

    def getSprite(self):
        return self.sprite

    def setSprite(self, newSprite):
        self.sprite = newSprite

    def getOrientation(self):
        return self.orientation

    def setOrientation(self, newOrientation):
        self.orientation = newOrientation

    def isFacingRight(self):
        return self.getOrientation() == Orientation.RIGHT

    def isFacingLeft(self):
        return self.getOrientation() == Orientation.LEFT

    def getHealth(self):
        return self.health

    def setHealth(self, newHealth):
        self.health = newHealth

    def getGuarding(self):
        return self.guarding

    def setGuarding(self, newGuardState):
        self.guarding = newGuardState

    def getAtking(self):
        return self.atking

    def setAtking(self, newAtking):
        self.atking = newAtking

    def getDamaged(self):
        return self.damaged

    def setDamaged(self, newDamaged):
        self.damaged = newDamaged

    def getFlicker(self):
        return self.flicker

    def setFlicker(self, newFlicker):
        self.flicker = newFlicker


class Orientation(Enum):
    RIGHT = 1
    LEFT = 0