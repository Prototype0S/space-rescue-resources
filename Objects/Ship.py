from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
import pygame

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        
        # register events
        self.handle_key_events = True
        self.can_shoot = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            #self.y -= 10
            self.y_speed -= 2
        elif key[pygame.K_s]:
            #self.y += 10
            self.y_speed += 2
        elif key[pygame.K_SPACE]:
            self.shoot_laser()

    def keep_in_room(self):
            """
            Keeps the ship inside the room
            """
            if self.y < 0:
                self.y = 0
                self.y_speed = 0
            elif self.y + self.height> Globals.SCREEN_HEIGHT:
                self.y = Globals.SCREEN_HEIGHT - self.height
                self.y_speed = 0

    def step(self):
        """ 
        Determine what happens to the ship on each click of the game clock
        """
        self.keep_in_room()
    def shoot_laser(self):
        #shoot a laser from the ship
        new_laser = Laser(self.room, self.x + self.width, self.y + self.height/ 2-4)
        self.room.add_room_object(new_laser)
        self.can_shoot = False
        self.set_timer(10,self.reset_shot)

    def reset_shot(self):
        #allows ship to shoot again
        self.can_shoot = True
    