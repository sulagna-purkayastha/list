a=int(input("enter number"))
b=1
d=a//2+(.5)
while b<=a:
    c=1
    while c<=a:
        if b==1 or b==a:
            print("*",end=" ")
        elif c==1:
            print("*",end=" ")
        elif c<=a:
            if c==a and b!=3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
        c=c+1
    print()
    b=b+1