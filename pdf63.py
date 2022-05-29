list = []
list_1 =[]
n = int(input("enter the total numbers inside list.: "))
i = 1
while(i <= n):
    num = int(input("enter the numbers you want to insert into list: "))
    i +=1
    list.append(num)
    print(list, " <--the given list by you is here.\n ")
    list.sort()
    print(list)
print(max(list))