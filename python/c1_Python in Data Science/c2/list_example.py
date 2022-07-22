my_list = ['alice', 'bob', 'mark', 'andrew']

print(my_list)
print(f'print first element of the list: {my_list[0]}')
print(f'print last element of the list: {my_list[-1]}')
print(f'the length of the list is {len(my_list)}')

my_list[2] = 'dimitry'
print(my_list)

my_list.append('alex')
print(my_list)

new_people = ['mark', 'gregory']
my_list.extend(new_people)
print(my_list)
my_list += new_people
print(my_list)

my_list.pop()
print(my_list)

my_list.pop()
print(my_list)
