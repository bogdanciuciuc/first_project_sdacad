# version 1
def count_upper_lower_1(word):
    upper = 0
    lower = 0
    for i in range(len(word)):
        if 122 >= ord(word[i]) >= 97:
            lower += 1
        elif 65 <= ord(word[i]) <= 90:
            upper += 1
    return upper, lower


# version 2
def count_upper_lower_2(word):
    upper = 0
    lower = 0
    for i in range(len(word)):
        if (word[i] == word[i].upper()) & (word[i] != chr(ord(' '))):
            upper += 1
        elif (word[i] == word[i].lower()) & (word[i] != chr(ord(' '))):
            lower += 1
    return upper, lower


print(f'version 1: {count_upper_lower_1("Ana Are Mere")}')
print(f'version 2: {count_upper_lower_2("Ana Are Mere")}')
