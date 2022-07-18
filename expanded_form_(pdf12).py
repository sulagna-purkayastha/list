# You will be given a number and you need to return it as a string in Expanded Form. 
# For example: 12 # Should return '10 + 2'
            #  42 # Should return '40 + 2'
            #  70304 # Should return '70000 + 300 + 4'


number=input("Enter no: ")
i=0
j=1
while i<len(number):
    a=number[i]
    b=int(len(number))-j
    c=b*"0"
    if int(a)>0:
        if i!=int(len(number)-1):
            print(str(a)+str(c)+"+",end="")
        elif i==int(len(number)-1):
            print(a,end="")
    i=i+1
    j=j+1
