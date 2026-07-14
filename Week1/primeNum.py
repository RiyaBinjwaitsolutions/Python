num=int(input("enter num: "))

if(num<=1):
    print("not prime")
else:
    isPrime=True

    for i in range (2,num):
        if(num%i==0):
            isPrime=False
            break

    if isPrime:
        print("Prime")
    else:
        print("not prime")
        
       