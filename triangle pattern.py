'''Author :Sreehari Pramod
   Date :19/11/2024'''

row=int(input("Enter the no of rows :"))
#Increasing triangle
for i in range(1,row+1):
    for j in range(i):
        print(a,end='')
    print()
print()
#Decreasing triangle
for i in range(row,0,-1):
    for j in range(i):
        print('*',end='')
    print()
print()
#Hill pattern
for i in range(1,row+1):
    for j in range(row-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()
print()
#Reverse hill pattern
for i in range(row,0,-1):
    for j in range(row-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()