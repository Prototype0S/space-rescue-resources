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
        self.laser_cooldown = 8  # Cooldown time for shooting lasers
        self.default_laser_cooldown = self.laser_cooldown  # Store the default cooldown time
        self.cooldown_boost_active = False
        self.register_collision_object("Package")
        self.register_collision_object("Zork")
        speed = 8
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        speed = 10
        if key[pygame.K_w]:
            #self.y -= 10
            self.y_speed -= 2
            if self.y_speed < -speed:
                self.y_speed = -speed
        elif key[pygame.K_s]:
            #self.y += 10
            self.y_speed += 2
            if self.y_speed > speed:
                self.y_speed = speed
        elif key[pygame.K_SPACE]:
            self.shoot_laser()
        elif key[pygame.K_a]:
            #self.x -= 10
            self.x_speed -= 2
            if self.x_speed < -speed:
                self.x_speed = -speed
        elif key[pygame.K_d]:
            #self.x += 10
            self.x_speed += 2
            if self.x_speed > speed:
                self.x_speed = speed
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
            if self.x < 0:
                self.x = 0
                self.x_speed = 0    
            elif self.x + self.width > Globals.SCREEN_WIDTH:
                self.x = Globals.SCREEN_WIDTH - self.width
                self.x_speed = 0

    def step(self):
        """ 
        Determine what happens to the ship on each click of the game clock
        """
        self.keep_in_room()
    def shoot_laser(self):
        #shoot a laser from the ship
        if self.can_shoot:
            new_laser = Laser(self.room, self.x + self.width, self.y + self.height / 2 - 4)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(self.laser_cooldown, self.reset_shot)
            self.room.shoot_laser.play()

    def reduce_laser_cooldown(self, amount=4):
        if not self.cooldown_boost_active:
            self.laser_cooldown = max(1, self.laser_cooldown - amount)
            print(f"Cooldown reduced to: {self.laser_cooldown}")
            self.cooldown_boost_active = True
            self.set_timer(int(15 * Globals.FPS), self.reset_laser_cooldown)

    def reset_laser_cooldown(self):
        print("Cooldown reset to default:", self.default_laser_cooldown)
        self.laser_cooldown = self.default_laser_cooldown
        self.cooldown_boost_active = False

    def reset_shot(self):
        #allows ship to shoot again
        self.can_shoot = True
    def handle_collision(self, other, other_type):
        if other_type == 'Package':
            print("Package collected!")
            self.reduce_laser_cooldown()
            self.room.delete_object(other)
            self.room.package_received.play()
        elif other_type == 'Zork':
            print("Zork hit!")
            self.room.delete_object(other)
            self.room.running = False

    