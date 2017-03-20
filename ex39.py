#ex39

# things = ['a','b','c','d']
# print things[1]
#
# things[1] = 'z'
# print things[1]
#
# things

states = {
    'oregon': 'OR',
    'florida': 'FL',
    'california': 'CA',
    'new york': 'NY',
    'michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['michigan']
print "Florida's abbreviation is: ", states['florida']

print '-' * 10
print "Michigan has: ", cities[states['michigan']]
print "Florida has: ", cities[states['florida']]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has the city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas')

if not state:
    print "Sorry no Texas"

city = cities.get('TX', "Does not exist")
print "The city for the state 'TX' is: %s" % city