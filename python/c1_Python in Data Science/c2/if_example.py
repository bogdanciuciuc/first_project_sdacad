print(3 < 5)
print(4 == 4)
print(3 != 3.0)
print(-1 > -5)

print(4 > 6 or 5 < 8)
print(4 > 6 and 5 < 8)

print(3 in [2, 3, 4])
print('d' not in 'car')

# Vrem sa afisam daca un numar citit de la tastatura este mai mic decat 10, intre 10 si 15 sau mai mare decat 15.
input_nb = int(input('type a number '))
if input_nb < 10:
    print(f'number {input_nb} < 10')
# elif 10 <= input_nb and input_nb <= 15:
elif 10 <= input_nb <= 15:
    print(f'number is between 10 and 15')
else:
    print(f'number {input_nb} > 15')
