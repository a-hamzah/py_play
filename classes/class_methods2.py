class Animal:
    def __new__(cls, legs):
        if legs == 2:
            return Biped()
        else:
            return NotBiped()


class Biped:
    def __init__(self):
        print("2 legged animal")


class NotBiped:
    def __init__(self):
        print("not 2 legged animal")


animal1 = Animal(legs=2)
animal2 = Animal(legs=9)
