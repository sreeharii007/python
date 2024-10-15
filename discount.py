#Creator :Sreehari Pramod
#Date :15-10-2024

amt=int(input("Enter purchase amount :"))
if amt>500:
    amt=amt-(0.2*amt)
    print("Payable amount :",amt)
elif amt>=200 and amt<=500:
    amt=amt-(0.1*amt)
    print("Payable amount :",amt)
else:
    print("Payable amount :", amt)
