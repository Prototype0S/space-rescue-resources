from GameFrame import RoomObject

class Astronaut(RoomObject):
    """
    Class for the astronauts escaping from Zork
    """
    
    def __init__(self,room,x,y):
        """
        Initialise the astronaut instance
        """
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        
        # set image
        image = self.load_image("Astronaut.png")
        self.set_image(image,50,49)
        
        # set travel direction
        self.set_direction(180, 5)
        
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
            self.room.delete_object(self)
            
    def outside_of_room(self):
        """
        removes astronauts that have exited the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)