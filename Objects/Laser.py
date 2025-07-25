from GameFrame import RoomObject, Globals

class Laser(RoomObject):
    """
    Class for the lasers shot by the Ship
    """
    
    def __init__(self, room, x, y):
        """
        Inistialise the laser
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Laser.png")
        self.set_image(image, 33, 9)
        self.fireball_timer = 0
        
        # set movement
        self.set_direction(0, 20)

        #handle events
        self.register_collision_object("Asteroid")
        self.register_collision_object("Astronaut")
        self.register_collision_object("Zork")
        
    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        self.outside_of_room()
        
    def outside_of_room(self):
        """
        removes laser if it has exited the room
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)
    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        if self.fireball_timer > 0:
            self.fireball_timer -= 1
            if self.fireball_timer == 0:
                self.room.delete_object(self)
            return  # Skip normal movement/deletion while fireball is active
        self.outside_of_room()

    def handle_collision(self, other, other_type):
        #Handle laser collisions with other registered objects
        if other_type == "Asteroid":
            self.room.delete_object(other)
            self.room.delete_object(self)
            self.room.score.update_score(5)
        elif other_type == "Astronaut":
            self.room.delete_object(other)
            self.room.delete_object(self)
            self.room.score.update_score(-10)
        elif other_type == "Zork":
            #self.room.delete_object(self)
            try:
                fireball = self.load_image("Fireball.png")
                self.set_image(fireball,50, 48)
                self.fireball_timer = int(0.125*Globals.FPS)
                self.set_direction(0, 0)  # Stop movement
            except Exception as e:
                print("Error loading Fireball.png:", e)
