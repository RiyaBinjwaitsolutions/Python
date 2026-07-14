def factorial(n):
    fact=1

    for i in range(1,n+1):
        fact =fact * i

    return fact

print (factorial(5))


factorial = lambda n: 1 if n==0 or n==1 else n*factorial(n-1)
print(factorial(5))
 