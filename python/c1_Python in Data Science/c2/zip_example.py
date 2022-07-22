people = ['alice', 'bob', 'mark', 'george', 'julia']
age = [23, 45, 12, 70, 36]

zipped_list = list(zip(people, age))
print('zipped list = ', zipped_list)

people2, age2 = zip(*zipped_list)
print(people2)
print(age2)

people2 = list(people2)
age2 = list(age2)

print(people2)
print(age2)

my_tuple = 1, 2, 3
print(my_tuple)
print(my_tuple[0])
