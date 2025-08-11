from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
from Objects.Astronaut import Astronaut
from Objects.Package import Package
from Objects.Laser import Laser
import random

class Zork(RoomObject):
    """
    A class for the game's antagoist
    """
    zork_health = 30  # Health of the Zork boss

    def __init__(self, room, x, y):
        """
        Initialise the Boss object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        
        # set inital movement
        self.y_speed = random.choice([-10, 10])
        self.type = "Zork"
        # start asteroid timer
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        
        # start astronaut timer
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)
        #start package timer
        package_spawn_time = random.randint(1, 1000)
        self.set_timer(package_spawn_time, self.spawn_package)
        self.register_collision_object("Ship")
        
    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
            
    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()
    
        
    def spawn_asteroid(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)
        
        # reset time for next Asteroid spawn
        if Globals.SCORE > 500:
            asteroid_spawn_time = random.randint(1, 50)
        elif Globals.SCORE > 400:
            asteroid_spawn_time = random.randint(1, 80)
        elif Globals.SCORE > 300:
            asteroid_spawn_time = random.randint(1, 100)
        else:
            asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
    def spawn_astronaut(self):
        """
        Randomly spawns a new astronaut
        """
        # spawn astronaut and add to room
        new_astronaut = Astronaut(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_astronaut)
        
        # reset timer for next astronaut spawn
        if Globals.SCORE > 400:
            astronaut_spawn_time = random.randint(1, 500)
        elif Globals.SCORE > 300:
            astronaut_spawn_time = random.randint(1, 300)
        else:
            astronaut_spawn_time = random.randint(1, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)
    def spawn_package(self):
        """
        Randomly spawns a new package
        """
        # spawn package and add to room
        new_package = Package(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_package)
        
        # reset time for next package spawn
        package_spawn_time = random.randint(1, 5000)
        self.set_timer(package_spawn_time, self.spawn_package)
    def handle_laser_hit(self, laser, other_type):
        """
        Handle the laser hit on Zork
        """
        zork_health = self.zork_health
        zork_health -= 1
        if zork_health <= 0:
            self.room.delete_object(self)
            self.room.score.update_score(100)

        if other_type == "Ship":
            self.room.delete_object(self)
            self.room.asteroid_collision.play()
            Globals.LIVES -= 3
            self.room.lives.update_image()            

