#ex5
# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this next line is tricky
print "If I add %d, %d and %d I get %d." %(age, height, weight, age + height + weight)

#study drills

print "Height is %f in centimeters." % (height * 2.54)
print "Weight is %f in kilograms." % (weight * .453592)

rounded_weight = round(weight * .453592)
print 'The kilo weight rounded is %f.' % rounded_weight