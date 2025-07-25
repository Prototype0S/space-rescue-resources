from GameFrame import Level, Globals
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Hud import Score, Lives

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Galaxy_image.png")
        
        # add objects
        self.add_room_object(Ship(self, 25, 50))
        self.add_room_object(Zork(self,1120, 50))
        
        # add HUD items
        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)
        self.lives = Lives(self, Globals.SCREEN_WIDTH - 150, 20)
        self.add_room_object(self.lives)
        self.shoot_laser = self.load_sound("Laser_shot.ogg")
        self.asteroid_shot = self.load_sound("Asteroid_shot.wav")
        self.astronaut_saved = self.load_sound("Astronaut_saved.ogg")
        self.asteroid_collision = self.load_sound("Ship_damage.ogg")
        self.astronaut_shot = self.load_sound("Astronaut_hit.ogg")
        self.zork_shot = self.load_sound("Zork_shot.ogg")