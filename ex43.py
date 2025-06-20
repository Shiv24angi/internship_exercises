from sys import exit
from random import randint

# Base Scene class
class Scene(object):
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

# Engine class
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n- - - - - - - - ")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

# Death scene
class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

# Central Corridor scene
class CentralCorridor(Scene):
    def enter(self):
        print("The Gothons of Planet Percal #25 have invaded your ship...")
        print("You're running down the central corridor when a Gothon jumps out.")
        
        action = input("> ")

        if action == "shoot!":
            print("You fire but miss. He shoots you. You die.")
            return 'death'

        elif action == "dodge!":
            print("You slip and die. Ouch.")
            return 'death'

        elif action == "tell a joke":
            print("You tell a joke. The Gothon laughs and you shoot him.")
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

# Laser Weapon Armory scene
class LaserWeaponArmory(Scene):
    def enter(self):
        print("You enter the armory and need to guess the 3-digit code.")
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("You got the bomb!")
            return 'the_bridge'
        else:
            print("The lock is sealed forever.")
            return 'death'

# The Bridge scene
class TheBridge(Scene):
    def enter(self):
        print("You burst onto the bridge with the bomb under your arm.")
        action = input("> ")

        if action == "throw the bomb":
            print("You panic and die.")
            return 'death'

        elif action == "slowly place the bomb":
            print("You place the bomb and escape.")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'

# Escape Pod scene
class EscapePod(Scene):
    def enter(self):
        print("You rush to the escape pod chamber. Pick one.")
        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        try:
            pod = int(guess)
        except ValueError:
            print("That's not a number!")
            return 'death'

        if pod != good_pod:
            print(f"You chose pod {pod}. It malfunctions. You die.")
            return 'death'
        else:
            print(f"You chose pod {pod}. It works! You escape. You won!")
            return 'finished'

# Finished scene
class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'

# Map class
class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# Game starts here
if __name__ == "__main__":
    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()
