num=[50,40,23,70,56,12,5,10,7]
a=0
sum=0
b=[]
while a<len(num):
    if num[a]>sum:
        sum=num[a]
    a=a+1
b.append(sum)
print(b)