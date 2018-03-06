class ATM:
	def __init__(self,balance,bank_name):
		self.withdrawls_list =[]
		self.balance = balance
		self.bank_name = bank_name

	def withdraw(self,request):
		print "Welcom To: " + self.bank_name
		print("Your balance Is: " +str(self.balance))
		pvals = [100,50,10,5,2,1]
		if request > self.balance:
			print "Can't give you this money !!"
		else:
			self.withdrawals_list.append(request)	
			for index in pvals:
				while request-index >=0:
					print ("give " +str(index))
					request -= index
					self.balance = self.balance - index
			print"=============================================="
	
	def show_withdrawals(self):
		print "***********************************************"
        print self.bank_name + " withdraws"
        for withdraw in self.withdrawls_list:
            print withdraw

