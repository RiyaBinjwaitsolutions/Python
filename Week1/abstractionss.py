from abc import ABC , abstractmethod

class Bank(ABC):
    
    @abstractmethod
    def interest_rate(self):
        pass

class SBI(Bank):

    def interest_rate(self):
        print("sbi interest rate is: 6%")

class HDFC(Bank):

    def interest_rate(self):
        print("interest is 10%")

h= HDFC()
s=SBI()

s.interest_rate()
h.interest_rate()

    
  

 