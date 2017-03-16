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
