set1 = {'pinky', 'brian', 'ceva'}
set2 = {'brian', 'ceva1', 'ceva2'}

print(set1 & set2)
print(set1 | set2)
print(set1 ^ set2)
print(set1 - set2)

dictionary = {'t-shirt': 2,
              'pants': 3,
              'socks': 4}

print(dictionary['socks'])
# print(dictionary['sosete'])       error because no such key in dictionary
#                                   will stop the program
print(dictionary.get('socks'))
print(dictionary.get('sosete'))  # prints None
print(dictionary.get('sosete', 'no sosete in dictionary'))  # prints our message

dictionary['sosete'] = 5
print(dictionary.get('sosete'))

dictionary_value_list = list(dictionary.values())
print(dictionary_value_list)

dictionary_key_list = list(dictionary.keys())
print(dictionary_key_list)

for letter in ['a', 'e', 'i', 'o', 'u']:
    a = 0
    for item in dictionary_key_list:
        if letter in item:
            print(f'item {item} has {letter} in it')
            a += 1
    if a == 0:
        print(f'no item has the letter {letter} in it')

a = 0
while a < 3:
    a += 1

print(a)
