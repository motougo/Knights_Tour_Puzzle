squares = []
n=int(input('\n'))

x=0
for count in range(n):
    num=int(input())
    if num%7 == 0:
        squares.insert(x,num*num)
        x += 1

for count in range(len(squares)):
    print(squares.pop(0))


