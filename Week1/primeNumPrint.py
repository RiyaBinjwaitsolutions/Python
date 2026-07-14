n=int(input("enter n: "))

for num in range(2,n+1):
    isPrime=True

    for i in range(2,num):
        if num%i==0:
            isPrime=False
            break
    if isPrime:
        print(num,end=" ")