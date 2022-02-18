numstring = input()
numlist = numstring.split()

target = input()

pos = 0
answer = []

for i in numlist:
    if i == target:
        answer.append(pos)
    pos += 1

if answer:
    for j in answer:
        print(j, ' ', end="")
else:
    print('not found')
