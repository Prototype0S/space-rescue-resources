from GameFrame import RoomObject
import random

class Package(RoomObject):
    """
    Class for the package escaping from Zork
    """
    
    def __init__(self,room,x,y):
        """
        Initialise the package instance
        """
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        self.type = "Package"
        # set image
        image = self.load_image("Repair_kit.png")
        self.set_image(image,42,42)
        
        # set travel direction
        self.set_direction(180, random.randint(3, 10))
        
        # handle events
        self.register_collision_object("Ship")
        
    def step(self):
        """
        Determines what happend to the astronaut on each tick of the game clock
        """
        self.outside_of_room()
        
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles the collision event for Astronaut objects
        """
        # ship collision
        if other_type == "Ship":
            if hasattr(other, "reduce_laser_cooldown"):
                other.reduce_laser_cooldown()
            self.room.delete_object(self)
            self.room.package_received.play()
            
    def outside_of_room(self):
        """
        removes packages that have exited the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)
            