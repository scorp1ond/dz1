class Car:

    manufacturer = "Unknown"
    num_wheels = 4
    num_seats = 5

    def __init__(self, model, color, year):

        self.model = model
        self.color = color
        self.year = year



car1 = Car("Toyota Camry", "blue", 2020)
car2 = Car("Tesla Model S", "black", 2022)
car3 = Car("Honda Civic", "red", 2019)


class Dog:

    species = "Canis familiaris"
    num_legs = 4
    sound = "Woof"

    def __init__(self, name, age, breed):

        self.name = name
        self.age = age
        self.breed = breed



dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "Labrador")
dog3 = Dog("Charlie", 2, "Poodle")