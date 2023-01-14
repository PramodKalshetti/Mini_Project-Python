#Program for validating Mobile Number ( must contain 10 digits)
#mobilevalid.py
import re
while(True):
	mno=input("Enter ur mobile number:")
	if(len(mno)==10):
		result=re.search	("\d{10}",mno)
		if(result!=None):
			print("Ur Mobile Number is valid:")
			break
		else:
			print("Ur Mobile Number should not contains strs/special symbols")
	else:
		print("Ur Mobile Number is invalid, bcoz It contains more than 10 digits:")

