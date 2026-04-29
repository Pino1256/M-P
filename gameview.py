import arcade
from sprite_animato import SpriteAnimato

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class Player(SpriteAnimato): 
    def __init__(self):
        super().__init__(scale = 1)

        file_animazioni = {
            "destra": "assets/run_right.png",
            "sinistra": "assets/run_left.png",
            "giu": "assets/run_down.png",
            "su": "assets/run_up.png",
            "idle": "assets/run_idle.png"
        }

        for dir, percorso in file_animazioni.items():
            self.aggiungi_animazione(
                nome = f"run_{dir}",
                percorso = percorso,
                frame_width = 96,
                frame_height = 80,
                num_frame = 8,
                colonne = 8,
                durata = 1
            )
        
        self.direzione = "idle"
        self.change_x = 0
        self.change_y = 0

    def update_animation(self, delta_time):
        if self.change_y > 0:
            self.direzione = "giu"
        elif self.change_y < 0:
            self.direzione = "giu"
        elif self.change_x > 0:
            self.direzione = "sinistra"
        elif self.change_x < 0:
            self.direzione = "destra"
        
        if self.change_x != 0 or self.change_y != 0:
            self.imposta_animazione(f"run{self.direzione}")
        else:
            self.direzione = "idle"
            self.imposta_animazione(f"run_{self.direzione}")
        
        super().update_animation(delta_time)

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