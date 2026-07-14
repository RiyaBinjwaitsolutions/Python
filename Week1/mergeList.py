n=int(input("enter size of L1: "))
L1=[]
m=int(input("enter size of L2: "))
L2=[]
for i in range(n):
    x=int(input())
    L1.append(x)
print(L1)

for i in range(m):
    x=int(input())
    L2.append(x)
print(L2)

L1.extend(L2)
print("Merged List: ",L1)
