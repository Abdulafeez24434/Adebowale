class Animal:

    status = "Animate" # CLASS ATTRIBUTE

    def __init__(self, limbs, covering, food_type, name, habitat, family ):
        self.limbs = limbs
        self.covering = covering
        self.food_type = food_type
        self.habitat = habitat
        self.family = family
        self.__name = name ##__NAME IS AN ENCAPSULATED ATTRIBUTE

    def set_Name(self, new_name): #SETTER FOR NAME BECAUSE NAME IS ENCAPSULATED
        self._name = new_name

    def get_Name(self):
        return self.__name





billy = Animal(name = "Billy", limbs = 4, covering = "fur", habitat = "Terrestrial", food_type = "Omnivore", family = "Dog")

rhodes = Animal(name = "Rhodes", limbs = 4, covering = "Feathers", habitat = "Aboreal", food_type = "Omnivore", family = "Bird")



print(type(billy))
print(billy.status)
print(billy.food_type)
print(billy.covering)

text1 = f"{rhodes.get_Name()} is a {rhodes.family} and dwells in {rhodes.habitat} habitat.\n"
text2 = f"{billy.get_Name()} is a {billy.family} and dwells in {billy.habitat} habitat."

print(text1, text2, sep = "\n")

class Dog(Animal):

    def __init__(self, breed, colour, limbs, covering, food_type, name, habitat, family ):
        Animal.__init__(self, limbs, covering, food_type, name, habitat, family )
        self.breed = breed
        self.colour = colour

    def bark(self):#self is a default first argument always required by an instance method
        print(f"Woof...!!!")


tiger = Dog(name = "Tiger", limbs = 4, covering = "fur", habitat = "Terrestrial", food_type = "Omnivore", family = "Dog", colour = "Brown", breed = "Alsatian")

print(tiger.breed)
print(tiger.bark())
