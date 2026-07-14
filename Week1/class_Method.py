class Student:
    
    school="ABC"

    def __init__(self,name):
        self.name=name
    
    @classmethod
    def change_school(cls,new_scl):
        cls.school=new_scl
    

s1=Student("riya")
s2=Student("shreya")
Student.change_school("XYZ")
print(s1.school)
print(s2.school)