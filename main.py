import character
import console
import world






class Game():
    def __init__(self):
        global character
        global console
        character = character.Character()
        console = console.Console()

    def startgame(self):
        
        console.status_("game is starting", "status")
        
        name = console.input_("please enter a name for your character:", "cyan-bold")

        confirmed = False
        while confirmed == False:
            confirmation = console.input_(f"would you like your new name to be {name}?", "yellow-bold")
            if confirmation == "yes":
                character.setName(name)
                console.output_(f"your new name has been set to {name}!", "green-bold")
                confirmed = True
            elif confirmation == "no":
                name = console.input_("please enter a name for your character:", "cyan-bold")
            else:
                console.output_(f"please enter a yes or no answer as confirmation!", "yellow-bold")
        
        global world
        world = world.World()




        self.gameloop()

    def gameloop(self):
        quitGame = False
        #global world
        #world = world.World()

        while quitGame == False:
            pass
            # game loop


















game = Game()
game.startgame()