import arcade
import random

def square(x,y):
    arcade.draw_lrtb_rectangle_filled(    
        x, # left
        x + 100, # right
        y + 100, # top
        y, # bottom
        arcade.color.RED
        )

arcade.open_window(1920, 1080, "test")
arcade.set_background_color(arcade.color.BABY_BLUE)

arcade.start_render()


for i in range(100):
    coords = [random.randint(0,1820), random.randint(0,980)]
    square(coords[0], coords[1])

























arcade.finish_render()


arcade.run()
