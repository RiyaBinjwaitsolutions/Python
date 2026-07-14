import math
class Shape:

    def area(self):
        print("calculate area")

class Circle(Shape):
    def __init__(self,radius):
         self.radius=radius
         

    def area(self):
         print(int(math.pi*(self.radius**2)))
    
class Rectangle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def area(self):
        print(self.height*self.width)

class triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def area(self):
        print(int(0.5*self.height*self.base))

C1=Circle(2)
C1.area()

R1=Rectangle(4,4)
R1.area()

T1=triangle(4,2)
T1.area()