def mobnum(num):
    if len(num)!=10 or num[0] not in '789':
        print("The number is not valid")
    else:
        print("The number is valid")
num=input("Input mobile number :")
mobnum(num)