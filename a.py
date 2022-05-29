a=1
b=int(input("enter number"))
c=0
e=0
while a<=b:
    wgt= int(input("enter weight"))
    hgt= int(input("enter hight"))
    e=e+hgt
    c=c+wgt
    if a==b:
        d=c//b
        print("average weight is",d)
    if a==b:
        f=e//b
        print("average hight is",f)
    a=a+1
