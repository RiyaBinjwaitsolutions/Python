age=int(input("enter age: "))
has_license=input("yes or no: ")
if age>=18:
    if(has_license=="yes"):
        print("can drive")
    else:
        print("not drive because of licence")
else:
    print("cannot drive")