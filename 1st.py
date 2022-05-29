numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
a=0
sum=0
while a<len(numbers):
    if numbers[a]>=20 and numbers[a]<=40:
        sum=sum+1
    a=a+1
print(sum)