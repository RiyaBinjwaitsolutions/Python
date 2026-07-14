data=True
line =1
word="store"
with open("sample.txt","r") as f:

    while data:

      data = f.readline()
      if(word in data):
         print(f"word:{word} found at line{line}")
         break
      
      print(data)
      line+=1