#Creator :Sreehari pramod
#Date :22-10-2024

temp=float(input("Enter the temperature :"))
que=input("Is the temperature in (C)elsius or (F)arenheit? :")
coverter=0
if que=='F':
    converter=(5/9)*(temp-32)
    print(temp,"farenheit is",converter,"celcius")
elif que=='C':
    converter=((9/5)*temp)+32
    print(temp,"celcius is",converter,"farenheit")
else:
    print("Answer the question with 'C' or 'F' only")