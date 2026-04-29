import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
    
        arcade.set_background_color(arcade.color.AERO_BLUE)
    
    def on_draw(self):
        self.clear()
    
    def on_update(self, delta_time):
        pass

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        return 
    
    def on_key_release(self, symbol: int, modifiers: int) -> bool | None:
        return 