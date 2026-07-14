num=int(input("enter number to reverse: "))
reverseNum=0
while num>0:
    lastdigit=num%10
    reverseNum = (reverseNum*10)+lastdigit
    num=num//10
print("reverseNum: ",reverseNum)
