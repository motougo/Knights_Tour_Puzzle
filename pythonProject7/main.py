text = input()
words = text.split()

test1 = 'https://'
test2 = 'http://'
test3 = 'www.'

answer = []

for word in words:
    lowerword = word.lower()
    if (lowerword.startswith(test1) or lowerword.startswith(test2) or lowerword.startswith(test3)):
        answer.append(word)

for i in answer:
    print(i)

