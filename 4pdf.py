# List product excluding duplicates.
# List = [6,1,3,5,6,3,1]
# Output: 60
list=[6,1,3,5,6,3,1]
a=0
b=[]
d=1
while a<len(list):
    if list[a] not in b:
        b.append(list[a])
        d=d*int(list[a])
    a=a+1
print(d)