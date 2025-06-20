from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    next_input = input("> ")
    if "0" in next_input or "1" in next_input:
        try:
            how_much = int(next_input)
        except ValueError:
            dead("That's not a valid number.")
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next_input = input("> ")

        if next_input == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next_input == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next_input == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next_input == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next_input = input("> ")

    if "flee" in next_input:
        start()
    elif "head" in next_input:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next_input = input("> ")

    if next_input == "left":
        bear_room()
    elif next_input == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
