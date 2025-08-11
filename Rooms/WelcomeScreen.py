from GameFrame import Level, Globals
from Objects.Title import Title
import pygame  # Add this import

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.bg_music = None
        Globals.SCORE = 0
        Globals.LIVES = 3
        # set background image
        self.set_background_image("Background.png")
        
        # add title object
        self.add_room_object(Title(self, 240, 200))
        # stop all sounds before playing music again
        pygame.mixer.stop()
        # load and play background music
        self.bg_music = self.load_sound("Music.mp3")
        self.bg_music.play(loops=1)