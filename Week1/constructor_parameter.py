class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name:",self.name)
        print("age:",self.age)

s1=Student("riya",21) #a constructor that accpets value while creating object is parameterized constructor
s1.display()
