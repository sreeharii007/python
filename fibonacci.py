def fibonacci():
    n = int(input("Enter a number :"))
    a=1
    b=0
    c=0
    while c<n:
        print(c,end=' ')
        c=a+b
        a=b
        b=c

