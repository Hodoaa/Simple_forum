Balnce = input("What is your Balnce? ")
print "----------------------------------"
print "Your Balnce is: ", Balnce
type(Balnce)
print "----------------------------------"
request = input("Plz Inter your request? ")
print "Your Request is? " ,request
print "----------------------------------"
pvals=[100,50,10,5,2,1]
if request <= Balnce:
    for index in pvals:
            while request - index >=0 :
                    print ("give " + str(index))
                    request -= index
else:
    print " request is begger than your Balnce"
