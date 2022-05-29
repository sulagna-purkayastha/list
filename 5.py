binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
i=0
c=0
while i<len(binary_number):
    b=binary_number[::-1]
    d=int(b[i])
    c=c+d*2**i
    i=i+1
    print(c)