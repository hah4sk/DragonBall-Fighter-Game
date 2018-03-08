import pygame


class Sprite:

    def __init__(self, filename, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.setImage(filename)

    def moveHorizontally(self, delta_x):
        self.x += delta_x

    def moveVertically(self, delta_y):
        self.y += delta_y

    def setX(self, newX):
        self.x = newX

    def setImage(self, newImageFilename):
        self.image = pygame.image.load(newImageFilename)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImage(self):
        return self.image

    def getWidth(self):
        return self.image.get_width()

    def getHeight(self):
        return self.image.get_height()

    def getHealth(self):
        return self.health

def collision(objectA, objectB):

        if(objectA.getX() <= objectB.getX() and objectA.getY() >= objectB.getY() and #to the left and down
        objectA.getX()+objectA.getWidth() >= objectB.getX() and objectA.getY() <= objectB.getY()+objectB.getHeight()):
            return True

        elif (objectA.getX() >= objectB.getX() and objectA.getY() >= objectB.getY() and #to the right and down
        objectB.getX()+objectB.getWidth() >= objectA.getX() and objectA.getY() <= objectB.getY()+objectB.getHeight()):
            return True

        elif (objectA.getX() <= objectB.getX() and objectA.getY() <= objectB.getY() and #to the left and up
             objectA.getX()+objectA.getWidth() >= objectB.getX() and objectA.getY()+objectA.getHeight() >= objectB.getY()):
            return True
        elif(objectA.getX() >= objectB.getX() and objectA.getY() <= objectB.getY() and #to the right and up
             objectB.getX()+objectB.getWidth() >= objectA.getX() and objectA.getY()+objectA.getHeight() >= objectB.getY()):
            return True

        return False