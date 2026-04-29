import arcade
from sprite_animato import SpriteAnimato

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
        
        self.direzione = "giu"
        self.change_x = 0
        self.change_y = 0



