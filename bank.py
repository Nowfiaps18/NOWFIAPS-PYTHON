class Bank:
    def __init__(self,accno,name,acctyp,bal):
        self.ac=accno
        self.n=name
        self.typ=acctyp
        self.b=bal
        
    def deposit(self,amt1):
        self.b+=amt1
        print("balance=",self.b)
        
    def withdraw(self,amt2):
        if self.b<amt2:
            print("insufficient balance")
        else:
            self.b-=amt2
            print("Balance=",self.b)
            
    def display(self):
        print("\nAccount No:",self.ac,"\nAccount Holder:",self.n,"\nAccount Type:",self.typ,"\nBalance:",self.b)
        print("MENU")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Display")
        print("4.Exit")

        
b1=Bank(1002,"Navya","Savings",0)
b1.display()


while True:
    choice=int(input("enter your choice:"))
    if choice==1:
        d=int(input("enter the amount to be deposited"))
        b1.deposit(d)
    elif choice==2:
        w=int(input("enter the amount to withdraw:"))
        b1.withdraw(w)
    elif choice==3:
        b1.display()
    elif choice>3:
        print("enter a valid choice")
    else:
        break
                
                           
        
        
