'''

Create animal base class with attribute and related methods then create sub concrete subclass using animal eg of subclass: cow, horse, dog

Create arithmetics class to calculate avg, mean, mode and standard deviation

Create a program to validate the age of the voter with the help of custom exception. Voters whose age is less than 18 should not be allowed to vote.

Create a program to check eligibility of the person for loan  with the help of oops concepts and exception handling. Person whose salary is less than 10K/ Month will not be eligible for the loan.

Solution for above 4: https://github.com/mayank-s-dev/PythonTraining/pull/3

'''
import random
import time


# Create a Bank Account in class which includes customer balance, day wise transactions, can transfer money to
# different person account, interest given to him with a specific percentage

class Bank:
    bank_name = 'Josh Bank of India'
    interest = 5
    customers = []
    interval = 1
    transactions = []

    def __init__(self, account_no):
        Bank.customers.append(self)
        self.account_no = account_no
        self.balance = 0
        self.transactions = []

    def get_balance(self):
        return self.balance

    def get_account_no(self):
        return self.account_no

    def get_transactions(self):
        return self.transactions

    def transfer(self, receiver_acc_no, sent_amount):
        if sent_amount > self.balance:
            print("Low Balance in senders account", self.account_no)
            return False

        self.balance -= sent_amount
        new_transaction = {
            "receiver_acc_no": receiver_acc_no,
            "sent_amount": sent_amount,
            "type_of_transactions": "Debited",
            "balance": self.balance
        }

        self.transactions.append(new_transaction)
        Bank.transactions.append(new_transaction)
        return True

    def settle_transfer(self, sender_acc_no, received_amt):
        self.deposit(received_amt)
        new_transaction = {
            "receiver_acc_no": sender_acc_no,
            "sent_amount": received_amt,
            "type_of_transactions": "Credited",
            "balance": self.balance
        }
        c2.transactions.append(new_transaction)
        Bank.transactions.append(new_transaction)

    def deposit(self, amount):
        self.balance += amount


def generate_acc_no():
    return random.randint(10000000, 99999999)


class Customer(Bank):
    def __init__(self, name):
        self.name = name
        self.account_no = generate_acc_no()
        super().__init__(self.account_no)


c1 = Customer("Mayank")
c1.deposit(500)

c2 = Customer("Rohit")
c2.deposit(800)

print("Before transfer", c1.name, c1.balance)
print("Before transfer", c2.name, c2.balance)
transfer_amt = 50
if c1.transfer(c2.account_no, transfer_amt):
    c2.settle_transfer(c1.account_no, transfer_amt)

print("Transaction1:", c1.name, "transferred", transfer_amt, "to", c2.name)
print("After transfer", c1.name, c1.balance)
print("After transfer", c2.name, c2.balance)

transfer_amt = 89
if c1.transfer(c2.account_no, transfer_amt):
    c2.settle_transfer(c1.account_no, transfer_amt)
# list if transfers
print(c1.name, c1.transactions)
print(c2.name, c2.transactions)

month = 1
while month <= 12:
    for customer in Bank.customers:
        interest_amt = round(customer.balance * Bank.interest) / 100
        customer.balance += interest_amt
        print("Interest of Rs", interest_amt, "deposited to customer", customer.account_no)

    time.sleep(Bank.interval)
    month += 1


for customer in Bank.customers:
    print("Customer", customer.name, "total balance after 1 year", round(customer.balance, 2))

