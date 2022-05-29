# Write a Python program to compute the average of n th elements in a given list of
# lists with different lengths.
# Original list:
# [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]
list= [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
n=0
a=0
while a<len(list[n]):
    b=0
    c=0
    while b<len(list):
        c=int(list[b][a])+c
        b=b+1
    avrg=c/(b+1)
    print(avrg)
    a=a+1