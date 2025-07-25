from GameFrame import RoomObject, TextObject, Globals

class Score(TextObject):
    """
    A class for displaying the current score
    """
    def __init__(self, room, x: int, y: int, text=None):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
        
    def update_score(self, change):
        """
        Updates the score and redraws the text
        """
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()
        
    def reset_score(self, chamge):
        Globals.SCORE = 0
        self.text = str(Globals.SCORE)
        self.update_text()

class Lives(RoomObject):
    '''
    A class for displaying the number of lives remaining
    '''
    def __init__(self, room, x: int, y: int):
        '''
        Initialises the lives object
        '''

        RoomObject.__init__(self, room, x, y)
        # set image
        self.lives_icon = []
        #Load the various lives images into a live list
        for index in range(6):
            self.lives_icon.append(self.load_image(f"Lives_frames/Lives_{index}.png"))
        self.update_image()

    def update_image(self):
        """
        Updates the number of lives on the UI"""
        
        self.set_image(self.lives_icon[Globals.LIVES], 125,23)