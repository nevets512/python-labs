'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class ModelCar:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase(self, more_speed):
        self.max_speed += more_speed

    def __str__(self):
        return f"The model is {self.model}, the year is {self.year} and the max speed is {self.max_speed} MPH."


BMW = ModelCar("M3", 2018, 220)
BMW.increase(5)

print(BMW)
