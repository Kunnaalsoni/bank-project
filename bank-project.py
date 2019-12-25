import sys
data={}


list1=["Name","Address","phone_no","govt_id","account_type","amount"]
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

def other_options(acc_num):
    ch = int(input("1.Check Balance\n2.Withdraw\n3.Deposite\n4.Close account\n5.Modify details\nEnter choice :"))

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

    elif ch == 4:
        del data[acc_num]
        print("Deleted")

    elif ch == 5:
        print("Choose what field you want to change")
        print("1.Name\n2.Address\n3.Phone No.\n4.Govt. ID\n5.Account Type")
        choice = input("Choice: ")
        if choice == "1":
            print("Existing name:")
            print(data[acc_num]["Name"])
            data[acc_num]["Name"] = input("Enter new name: ")
            print("Successfull")

        elif choice =="2":
            print("Existing Address:")
            print(data[acc_num]["Address"])
            data[acc_num]["Address"] = input("Enter new address: ")
            print("Successfull")

        elif choice == "3":
            print("Existing Phone No.: ")
            print(data[acc_num]["phone_no"])
            data[acc_num]["phone_no"] = input("Enter new mobile number: ")
            print("Successfull")

        elif choice == "4":
            print("Existing Govt ID: ")
            print(data[acc_num]["govt_id"])
            data[acc_num]["govt_id"] = input("Enter new Govt. ID type: ")
            print("Successfull")

        elif choice == "5":
            print("Existing type of account:")
            print(data[acc_num]["account_type"])
            data[acc_num]["account_type"] = input("Enter new type: ")
            print("Successfull")
        else:
            print("Please enter a valid choice")


    else:
        print("Please Enter a valid choice")



while True:
    list2=[]
    ch=int(input("1.New Customer\n2.Existing Customer\n3.Exit\nEnter choice:"))

    if ch == 1:
        take_data()

    elif ch == 2:
        acc_num = input("Enter your account number. :")
        if acc_num in data:
            print("Record found")
            other_options(acc_num)
        else:
            print("Record not found.")

    elif ch == 3:
        print("Thank you for using my program.")
        print("--BY PARV JOSHI")
        sys.exit()

    else:
        print("Please enter a valid choice")
