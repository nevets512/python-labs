'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
r = 3.14
pi = 3.142
h = 5

volume = (((r * r) * pi) * h)

print(volume)

surface = ((pi * 2) * (r * r)) + ((pi * 2) * r * h)

print(surface)
