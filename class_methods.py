

# Example of using __new__ and __init__ at the same time

class Person:
    def __new__(cls, name, age):
        # creating a new person object
        instance = object.__new__(cls)
        return instance

    def __init__(self, name, age):
        # initializing a new person object
        self.name = name
        self.age = age


person = Person("John Doe", 30)
print(f"Name = {person.name}, Age = {person.age}")
