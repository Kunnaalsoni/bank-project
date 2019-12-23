#bank project

data={}
list1=["Name :","Address :","Phone No. :","Govt. ID :","Account Type :","Amount"]
for foo in data:
    print(data[foo])
def take_data():

	acc_num = input("Enter account no. :")
		
	for item in list1:
		list2.append(input("Enter %s:"%item))

	data[acc_num] = dict(zip(list1,list2))
	print("Account Created")
	print("________________________________________________________________________________")
	return 0

def other_options():
	ch = int(input("1.Check Balance\n2.Withdraw\n3.Deposite\n4. Close account\nEnter choice :"))
	if ch == 1:
		print("Available Balance:",data[acc_num]["Amount"])
		print("________________________________________________________________________________")
	elif ch == 2:
		amt = int(input("Amount to withdraw."))
		new_amt = int(data[acc_num]["Amount"])- amt
		data[acc_num]["Amount"] = new_amt
		print("________________________________________________________________________________")
		print("Withdrawn successful.")
		print("Available Balance:",data[acc_num]["Amount"])
		print("________________________________________________________________________________")
	elif ch == 3:
		amt = int(input("Amount to Deposite."))
		new_amt = int(data[acc_num]["Amount"]) + amt
		data[acc_num]["Amount"] = new_amt
		print("________________________________________________________________________________")
		print("Deposite successful.")
		print("Available Balance:",data[acc_num]["Amount"])
		print("________________________________________________________________________________")
    elif ch == 4 :
        print("Hello")
	
while True:
	list2=[]
	ch=int(input("1.New Customer\n2.Existing Customer\n3.Exit\nEnter choice:"))
	
	if ch == 1:
		take_data()
	
	elif ch == 2:
		acc_num = input("Enter your account number. :")
		if acc_num in data:
			print("Record found")
			other_options()
		else:
			print("Record not found.")

print("Thank you for using my program.")
print("--BY PARV JOSHI")