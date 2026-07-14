nums=[12,23,34,12,23,56,78]
unique=[]
for num in nums:
    if num not in unique:
        unique.append(num)

print(unique)
