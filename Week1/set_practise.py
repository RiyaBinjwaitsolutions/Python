s={12,13,14,15,16}
s.add(18)
print(s)
s.remove(13)
print(s)
print(12 in s)

#removes duplicate from list
L1=[12,13,14,14]
print(list(set(L1)))

#find common
A={12,13,14}
B={1,2,3,4}
print(A&B)

# find all duplicate element from list
nums=[1,2,3,4,32,1,3,2]
seen=set()
duplicate=set()
for num in nums:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)
print(duplicate)