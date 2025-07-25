from GameFrame import Level
from Objects.Title import Title

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
        
        # add title object
        self.add_room_object(Title(self, 240, 200))
        # load sounds
        self.bg_music = self.load_sound("Music.mp3")
        
        # play background music
        self.bg_music.play(loops=1)