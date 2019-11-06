class person()
    has_mouth = True
    has_eyes  = True
    line1 = List(" 0               ")
    Line2 = List(" |               ")
    Line3 = List(" /               ")
    Line4 = List("/__|_____________")

    def __init__(self,name):
            self.name = name
            slef.age =age

    def walk(self, steps):
        self.display_position()

        for _ in range(steps):
            self.line1.pop(-1)
            self.line1.insert(0," ")
            self.line2.pop(-1)
            self.line2.insert(0," ") 
            self.line3.pop(-1)
            self.line3.insert(0," ")
            self.line4.pop(-1)
            self.line4.insert(0," ")
        self.display_position()
        

           


person1 = Person(name ="John")
print(person1. name)
print(person1. has_mouth)

person2 = Person(name = "Paul")
print("Before change of nname :", person2.name)
person2. name = "John"
print("After change of name :",person2.name)
print(person2.has_mouth)


