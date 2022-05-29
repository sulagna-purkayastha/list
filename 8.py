magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
a=0
while len(magic_square)>a:
    b=0
    row=0
    while len(magic_square[a])>b:
        row =row+magic_square[a][b]
        b=b+1
    print(row)
    a=a+1
b=0
a=0
col=0
while len(magic_square)>a:
    while len(magic_square[a])>b:
        col =col+magic_square[a][b]
        b=b+1
    print(col)
    a=a+1
a=0
b=0
dig=0
while len(magic_square)>a:
    while len(magic_square[a])>b:
        if a==b:
            c=magic_square[a][b]
            dig=dig+c
            break
        b=b+1
    a=a+1
print(dig)
a=0
b=0
dig2=0
c=len(magic_square[a])-1
while len(magic_square)>a:
    while len(magic_square[a])>b:
        if a==b:
            c=magic_square[a][b]
            dig2=dig2+c
            break
        b=b+1
    a=a+1
print(dig2)
if row==col and dig==dig2 and row == dig:
    print("its a magic square")
else:
    print("its not a magic square")