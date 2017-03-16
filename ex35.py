#ex35

from sys import exit

def gold_room():
    print "This room is full of gold! How much do we take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = float(choice)
    else:
        dead('Man, learn to type a number.')

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit()
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear in here!"
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door"
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved away from the door."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear is pissed and bites you")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "No idea what that means"
            exit()



def cthulu_room():
    print "Here you see the great evil, Cthulu"
    print "It stares at you and you go insane"
    print "Do you flee for you life or eat your own head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulu_room()

def dead(why):
    print why, "Good Job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right & left."
    print "Which one do you go through?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You starve.")

start()