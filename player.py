import arcade
from sprite_animato import SpriteAnimato

class Player(SpriteAnimato): 
    def __init__(self):
        super().__init__(scale = 1)

        self.file_animazioni = {
            "diestra": "assets/"
        }