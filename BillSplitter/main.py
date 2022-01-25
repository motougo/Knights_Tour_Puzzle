import random

numFriends=int(input('Enter the number of friends joining (including you):\n'))

if numFriends <= 0:
    print('\nNo one is joining for the party')
else:
    friends = {}
    print('\nEnter the name of every friend (including you), each on a new line:')
    for countFriend in range(numFriends):
        name = input()
        friends[name] = 0

    billValue = float(input('\nEnter the total bill value: \n'))

    ans = input('\nDo you want to use the "Who is Lucky?" feature?  Write Yes/No:\n')

    if ans == 'Yes':
        luckyOne = random.choice(list(friends.keys()))
        print(sep='')
        print(luckyOne, 'is the lucky one!')
        shareValue = round(billValue / (numFriends - 1), 2)
    else:
        luckyOne = ''
        print('\nNo one is going to be lucky')
        shareValue = round(billValue / numFriends, 2)

    for key in friends.keys():
        if key == luckyOne:
            friends.update({key: 0})
        else:
            friends.update({key: shareValue})

    print(sep='')
    print(friends)
