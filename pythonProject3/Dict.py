squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}

key = int(input())

print(squares.get(key,'There is no such key'))
squares.pop(key,'')
print(squares)
