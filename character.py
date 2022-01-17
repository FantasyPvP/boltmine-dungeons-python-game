from console import *
from world import *

class Character():
    def __init__(self):
        self.pos = [0,0]
        self.inventory = [
            "empty","empty","empty","empty","empty","empty","empty","empty","empty","empty",
            "empty","empty","empty","empty","empty","empty","empty","empty","empty","empty",
            "empty","empty","empty","empty","empty","empty","empty","empty","empty","empty"
        ]
        self.name = "empty"
        return

    def setName(self, name):
        self.oldName = self.name
        self.name = name

    def move(self, direction):
        if direction == "posx":
            self.pos[0] += 1
        if direction == "negx":
            self.pos[0] -= 1
        if direction == "posy":
            self.pos[1] += 1
        if direction == "negy":
            self.pos[1] -= 1
    
    def createCharacter(self, baseHealth, health, strength, speed, stamina, inventory):
        self.baseHealth = baseHealth
        self.health = health

        # strength works in a more unusual way than the other variables. the first value is a multiplier
        # whereas the second value is an addition, this means that the damage of the weapon in use is multiplied by the
        # first strength value and then added to the second value
        
        self.strength = strength
        self.speed = speed
        self.stamina = stamina
        for item in inventory:
            self.addItem(item)
        
    def addItem(self, item):
        found = False
        for slot in range(len(inventory)):
            if inventory[slot] != "empty":
                inventory[slot] = item
                found = True
                return(True)
        if found == False:
            return(False)
        
    