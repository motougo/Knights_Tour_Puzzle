vowels = 'aeiou'
# create your list here
word = ''
word = input()
vowel_list = [letter for letter in word if vowels.find(letter) >= 0]
print(vowel_list)
