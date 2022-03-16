# read animals.txt
# and write animals_new.txt

read_file = open('animals.txt', 'r', encoding='utf-8')
write_file = open('animals_new.txt', 'w', encoding='utf-8')

for name in read_file:
    write_name = name.strip()
    write_file.write(write_name + ' ')

read_file.close()
write_file.close()
