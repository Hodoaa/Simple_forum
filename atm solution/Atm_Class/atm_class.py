# i creat a file with name"Atmc.py" which contain the ATM as a class and WITHDRAW as function
# then here i load the class ATM from the file Atmc.py by the folwing line 
from Atmc import ATM

balance1 = 500
balance2 = 1000
balance3 = 20000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")
atm3 = ATM(balance3, "Cairo Bank")

atm1.withdraw(600)
atm1.withdraw(200)
atm1.withdraw(23)
atm1.withdraw(50)

atm2.withdraw(50)
atm2.withdraw(70)
atm2.withdraw(30)
atm2.withdraw(100)

atm3.withdraw(533)
atm3.withdraw(100)
atm3.withdraw(499)
atm3.withdraw(600)
