#ex31

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There is a giant bear here eating cheese cake.  What do you do?"
    print "1 - Take cake"
    print "2 - Scream at bear"

    bear = raw_input("> ")

    if bear == "1":
        print "The bear has eaten your face off. Good work!"
    elif bear == "2":
        print "The bear has eaten your legs off.  Good work!"
    else:
        print "Well, doing %s is probably better. Bears run away." % bear

elif door == "2":
    print " You stare into the endless abyss at Cthulu's retina."
    print "1 - Blueberry"
    print "2 - Yellow submarine"
    print "3 - Shotgun Monkey"

    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "You have survived by your mind is now jello"
    else:
        print "You have gone completely insane"
        
else:
    print "You stumble around and fall on the ground"
         
    
        

    
