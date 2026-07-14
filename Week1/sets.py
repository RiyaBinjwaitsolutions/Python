s={10,20,30}
print(s)
s={10,10,20,30} #duplicate elements removed automatically
print(s) 
# s={}  <class 'dict'> (if we pass empty curly braces it will make it dictionary)
s1=set() #for empty set
print(type(s)) #<class 'set'>
s1.add(40) #adding element at last
print(s1)
s1.update([30,40,50]) #add collection like list , tuples in random manner 
print(s1)
s.remove(20) #remove specific element
print(s)
# s.remove(100) #give error as element does not exist so use discard
#print(s)
s.discard(100)
print(s)
s.pop()#removes random element because sets are unordered
print(s)
s.clear()
print(s)
# loops in set
s={10,20,30}
for x in s:
    print(x)

#set operations
#Union - All unique elements
A={12,13,34,12}
B={13,33,56,57}
print(A | B)
print(A.union(B))

#Intersection - All common elements
print(A&B)
print(A.intersection(B))

#Difference - Elements present in A but not in B
print(A-B)

#symmetric difference - element present in either set but not both
print(A^B)
 
#subset and superset
A={1,2}
B={1,2,3,4}
print(A.issubset(B))
print(B.issuperset(A))

#built in functions
print(len(s))
print(max(s))
print(min(s))
print(sum(s))

#converting list to set
nums=[10,20,30,10]
unique = set(nums) #removes duplicate automatically
print(unique)

#frozen set - A frozen set is immutable
fs=frozenset([10,20,30])
print(fs)






