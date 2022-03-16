#  write your code here 
file = open('.\data\dataset\input.txt', 'r')
count = 0
for line in file:
    if line.strip() == 'summer':
        count += 1
file.close()
print(count)