# tuples, lists, sets, dictionaries

# Tuples
# indexed, ordered, unchangeable, allow duplication
name = "Hamza"
print(len(name))
cities = ("Lahore", "Karachi", "Islamabad", "Multan", "Multan")
animals = ("Hen", "Sparrow", "Parrot")
print(cities)
print(len(cities))
print(cities[3])

numberTuple = (1, 3, 5, 7, 9)
print(numberTuple)

Employee1 = ("Kumail", "26", "Manager")
Employee2 = ("Asad", 23 , "Janitor")
Employee3 = ("Usama", 24, "Worker")

print(Employee1)

# Lists
# Ordered, indexed, changeable, duplication

randomlist = ["furqan", "saad", "fahim"]
print(randomlist)

randomlist[0] = "hamza"
print(randomlist)
print(len(randomlist))

# Sets
# un-ordered, un-indexed, no duplication

randomset = {'Hamza', "Saad"}
print(randomset)
# print(randomset[1])

# Dictionaries
# unorderd, changeable, no duplication

car1 = {
    "company" : "BMW",
    "model" : 2018,
    "color" : "Red",
}

print(car1["color"])