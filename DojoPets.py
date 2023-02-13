class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.energy = 0
        self.health = 0

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print("Woof!")

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

pluto = Pet("Pluto", "dog", ["roll over", "sit"])
ninja = Ninja("Jorge", "Leon", ["bone"], ["kibble"], pluto)

ninja.walk().feed().bathe()
