def withdraw(Balance,request):
	Current_Balance = 0
	pvals=[100,50,10,5,2,1]
	if request <= Balance:
		for index in pvals:
			while request - index >=0:
				print("give " + str(index))
				request -= index
				Current_Balance = Current_Balance+index
		print ("Current_Balance is:  ") , Balance - Current_Balance
	else:
		print "Can't give you this money !!"
		
Balance = 500
print withdraw(Balance,278)
print withdraw(Balance,600)
print withdraw(Balance,5)
print withdraw(Balance,500)