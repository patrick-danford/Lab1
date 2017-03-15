#ex4

#variable for amount of cars
cars = 100

#variable for amount of space in each car
space_in_a_car = 4.0

#variable for amount of drivers
drivers = 30

#variable for amount of passengers
passengers = 90

#variable for calculation of cars not driven
cars_not_driven = cars - drivers

#variable for amount of cars driven
cars_driven = drivers

#variable for calculation of carpool capacity
carpool_capacity = cars_driven * space_in_a_car

#variable for calculation of average per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

