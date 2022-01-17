class Player():
    def __init__(self, inventory, health, pos):
        self.inventory = inventory
        self.health = health
        self.pos = pos

    def move(self, direction):
        if direction == "N":
            self.pos[1] += 1
        elif direction == "S":
            self.pos[1] -= 1
        elif direction == "E":
            self.pos[0] += 1
        elif direction == "W":
            self.pos[0] -= 1
        else:
            return(False)
        return(True)


    def pickup(self, item):
        self.inventory.append(item)

    def drop(self, slot):
        self.inventory.pop(item)



class World():
    def __init__(self):
        world = {
            00 : "spawn-point"
        }



def main():
    return




main()
