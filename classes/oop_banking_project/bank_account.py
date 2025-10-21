# The class is receiving an exception in the param with the pass statement
class BalanceException(Exception):
    # This class is used for exception handling if we don't have enough money in the account to make a transaction.
    pass



class BankAccount():
    #Lets create a Bank Account here:
    # fields are the amount and the name of the account
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount # balance amount
        self.name = acctName # name on the account
        print(f"\nAccount '{self.name}' created.\n Balance = ${self.balance:.2f}")
        # The :.2f is 2 decimal points for our formatting of the amount.
        
    
        
        #This will output the fields above printing the account name and balance.
    def getBalance(self):
        # Use the self field to capture self.balance and self.name
        print(f"\n Account '{self.name}' balance = ${self.balance:.2f}")
        
    # Lets create an deposit account so the user can add more money to their current balance.
    def deposit(self, amount):
        self.balance = self.balance + amount
        # current balance + new-amount provided in the param
        print("\nDeposit Balance.")
        self.getBalance()# calls upon the new updated balance
        
        
    def viableTransaction(self, amount):
        # if the current balance is greater then or equal to the amount submitted into the param then we can complete the transaction.
        if self.balance >= amount:
            return
        #else, return the balance exception error (with the current balance)
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)#Pass in the amount you wish to withdraw from the current balance.
            self.balance = self.balance - amount
            # So if the user has a current balance of $1000 but wants to withdraw $5000 
            # Any withdraw of an amount that the user doesn't have will result in an error message. 
        # This is because the amount the user wants to withdraw is too high, forcing the current balance to subtract 
        # from the new amount making it false as a negative number based on our if else statement above
            print("\nWithdraw complete.")
            #Otherwise, withdraw transaction successful!!!!!
            self.getBalance()
            # Our exception error
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
            
            
        # Let's transfer from one account to another. 
        # Need to withdraw from one account and deposit into another.
    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer...🚀')
            self.viableTransaction(amount) # Makes sure the transaction is valid before proceeding.
            self.withdraw(amount) # The amount needed for withdrawing
            account.deposit(amount) # the account we are transferring the money to
            print("\nTransfer complete! ✅\n\n**********")
        except BalanceException as error:
               print(f"\nTransfer interrupted. ❌ {error}")
               # error message when the user doesn't have the proper funds to transfer between accounts.
               
               
               

class InterestRewardsAcct(BankAccount):
    # An interest account of 5% added to the balance. 
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()
        
        

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
            
        self.fee = 5
        
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
            
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")