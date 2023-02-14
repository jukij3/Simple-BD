def read_from_file(filename):
    file = open(filename, 'r')
    names = tuple(file.readline()[:-1].split(','))
    data = []
    for line in file:
        line = line.split(',')
        data.append((int(line[0]), str(line[1]), line[2], int(line[3]), int(line[4]), line[5][:-1]))
    names_str = ''.join([str(each).ljust(15) for each in names])
    print(names_str)
    for tup in data:
        tup_str = ''.join([str(each).ljust(15) for each in tup])
        print(tup_str)
    return names, data


def write_to_file(names, data):
    file = open('d2.csv', 'w')
    file.write(','.join(names)+'\n')
    for line in data:
        line = [str(i) for i in line]
        file.write(','.join(line)+'\n')
    return file


def new_data(file_name):
    new_data = []
    file = open(file_name, 'a')
    i = 0
    while i <= 5:
        new = input()
        new_data.append(new)
        i += 1
    file.write(','.join(new_data) + '\n')


names, data = read_from_file('data.csv')
write_to_file(names, data)
print("Ввести данные?")
print("1) Yes")
print("2) No")
print("3) Удалить последнюю строку")
answer = input()
if answer == '1':
    new_data('data.csv')
elif answer == '3':
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        lines = lines[:-1]
    with open('data.csv', 'w') as file:
        file.writelines(lines)
else:
    exit()