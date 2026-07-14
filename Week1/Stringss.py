name="riya"
firstch=name[0]
print(firstch)
print(name[1:3]) #slicing
print(name[::-1])#reverse
print("hi"*3)
print("ri" in name)
print("java" in name)
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
s=" patidar "
print(s.strip())
print(name.replace("riya","tiya"))
print(s.count("a"))
print(s.find("a"))
print(s.startswith(" pa"))
print(s.endswith("ya"))
Str="apple mango banana"
print(Str.split())
words=['apple', 'mango', 'banana']
print("-".join(words))
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print("RIYA".islower())
print("riya".isupper())
for ch in name:
    print(ch)

s=input("enter string")
count=0
for ch in s:
    if ch.lower() in "aeiou":
        count+=1
print(count)

