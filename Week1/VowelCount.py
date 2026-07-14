name=input("enter name:")
count=0;
for ch in name:
    if(ch in "aeiouAEIOU"):
        count +=1
print("number of vowels: ",count)
