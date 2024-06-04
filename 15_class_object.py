h = ["credit","debit"]
a = int(input("enter your account number:\n"))
d = int(input("enter your account number to confirm:\n"))
while(d != a):
    d = int(input("enter your correct account number to confirm:\n"))
g = str(input("enter your method from credit or debit only:\n"))
while(g not in h):
    g = str(input("please, enter your method from credit or debit only:\n"))
e = int(input("enter your bank balance:\n"))
f = int(input(f"enter your money which you want {g}:\n"))
class Bank:
    def __init__(self,bal,acc):
        self.bal=bal
        self.account_number=acc
    def CD(self, meth,money):
        self.meth = meth
        self.money = money
        if(self.meth == "credit"):
            b = int(input("enter your account number:\n"))
            while(b != a):
                b = int(input("it is invalid,enter your account number:\n"))            
            self.bal+=self.money
            print("₹"+str(self.money),"credited\nTotal:","₹"+str(self.bal))
        if(self.meth == "debit"):
            c = int(input("enter your account number:\n"))
            while(c != a):
                c = int(input("it is invalid,enter your account number:\n"))
            
            self.money = money
            self.bal-=self.money
            print("₹"+str(self.money),"debited\nTotal:","₹"+str(self.bal))
account1 = Bank(e,a)
account1.CD(g, f)