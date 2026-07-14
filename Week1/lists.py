ListL1=["apple","mango",1,2,32]
ListL1.append(34)
print(ListL1)
ListL1.insert(0,56)
print(ListL1)
ListL1.extend([23,22,21])
print(ListL1)
ListL1.pop(0) #removes by index
print(ListL1)
ListL1.remove("mango") #remove by value
print(ListL1)

ListL1.pop() #remove last element
print(ListL1)
print(ListL1.index(2)) #accessing element
print(ListL1.count(2))

ListL1.reverse() #reversing list
print(ListL1)

ListL2=ListL1.copy() #copying list
print(ListL2)

ListL3=[12,23,34]
print("sum",sum(ListL3))
print("min element" ,min(ListL3))
print("max element",max(ListL3))

#Looping through list
for num in ListL3:
    print(num)


ListL4=[12,45,23,56]
ListL4.sort()
print(ListL4)
