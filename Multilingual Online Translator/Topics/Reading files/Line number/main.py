# read sample.txt and print the number of lines
file = open('sample.txt', 'r')
count = 0
for line in file:
    count += 1
file.close()
print(count)