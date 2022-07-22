my_list = ['alice', 'bob', 'mark', 'andrew', 'mark', 'gregory']

print(f'first 3 items {my_list[0:3]}')
print(f'first 3 items {my_list[:3]}')

print(f'index 2 till the end {my_list[2:]}')

# step 2
print(my_list[0:6:2])
print(my_list[::2])

# reverse order
print(my_list[::-1])
print(my_list[-1:-4:-1])
print(my_list[-3:])
