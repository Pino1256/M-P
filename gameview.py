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
            self.direzione = "su"
        elif self.change_y < 0:
            self.direzione = "giu"
        elif self.change_x > 0:
            self.direzione = "destra"
        elif self.change_x < 0:
            self.direzione = "sinistra"
        
        if self.change_x != 0 or self.change_y != 0:
            self.imposta_animazione(f"run_{self.direzione}")
        else:
            self.direzione = "idle"
            self.imposta_animazione(f"run_{self.direzione}")
        
        super().update_animation(delta_time)

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.AERO_BLUE)

        #personaggio
        self.personaggio = None
        self.lista_personaggio = arcade.SpriteList()
        self.speed = 5

        # movimento
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        self.setup()
    
    def setup(self):
        self.personaggio = Player()
        self.lista_personaggio.append(self.personaggio)

    
    def on_draw(self):
        self.clear()

        self.lista_personaggio.draw()
    
    def on_update(self, delta_time):

        cy = 0
        cx = 0

        self.lista_personaggio.update()
        self.lista_personaggio.update_animation(delta_time)

        if self.up_pressed: cy += self.speed
        if self.down_pressed: cy -= self.speed
        if self.left_pressed: cx -= self.speed
        if self.right_pressed: cx += self.speed
    
        self.personaggio.change_x = cx
        self.personaggio.change_y = cy


    def on_key_press(self, tasto, modificatori):

        if tasto in (arcade.key.UP, arcade.key.W):
            self.up_pressed = True
        elif tasto in (arcade.key.DOWN, arcade.key.S):
            self.down_pressed = True
        elif tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = True
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = True  
        
    
    def on_key_release(self, tasto, modificatori):

        if tasto in (arcade.key.UP, arcade.key.W):
            self.up_pressed = False
        elif tasto in (arcade.key.DOWN, arcade.key.S):
            self.down_pressed = False
        elif tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = False
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = False   
