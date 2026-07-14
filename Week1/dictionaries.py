student={
    "name":"Riya",
    "age":21
}
print(student["name"])
print(student.get("age")) #get is safer as if the dictionary did not contain key it will not throw error it simply outputs none

student["marks"]=42 #adding new key-value pair in student
print(student)

student["age"]=22
print("after updating age",student)

student.pop("age")
print("after removing age",student)

student.popitem()
print("after removing: ",student)

del student["name"]
print(student)

student={
    "name":"Riya",
    "age":21
}
print(student.keys())
print(student.values())
print(student.items())

student.update({
    "marks":32,
    "city":"indore"
})

print(student)

for key in student:
    print(key)

print("\n")
for values in student.values():
    print(values)

print("\n")

for key,value in student.items():
    print(key,value)

student ={
    101:{
        "name":"riya",
        "age":21,
        "marks":32

    },

    102:{
        "name":"Shreya",
        "age":18,
        "marks":34
    }
}

print("\n",student[101]["name"])



