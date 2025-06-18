from GameFrame import TextObject, Globals

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