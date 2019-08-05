'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

i = 2
f = 2.0

print (type(i))
print (type(f))

i = float(i)
print (type(i))

f = int(f)
print (type(f))

print (i / f)

# user input is *always* gathered as a string
# and needs to be converted if we want something else


miles = input("How many miles: ")
miles = float(miles)
minutes = input("How many minutes: ")
minutes = float(minutes)
mpm = (minutes / miles)
mph = (60 / mpm)
kph = (mph * 1.6)
print (kph)
