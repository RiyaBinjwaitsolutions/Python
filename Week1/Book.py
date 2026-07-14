class Book:
     
     def __init__(self,title,author):
          self.title=title
          self.author=author
          self.review=[]

     def add_review(self,new_review):
          self.review.append(new_review)

     def count_review(self):
          print(len(self.review))

     def display_review(self):
            print(self.review)

B1=Book("code of destiny","anuj mehta")
B1.add_review("fantastic")
B1.add_review("Excellent book")
B1.add_review("very good")
B1.add_review("good")
B1.count_review()
B1.display_review()