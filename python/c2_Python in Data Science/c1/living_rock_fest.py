# 1. Bug in lista de formatii la festival
#
# Avem o lista de formatii care participa la festivalul Living Rock de pe plaja Tuzla. Dintr-un bug al platformei,
# headlinerii sunt inversati cu ultima formatie de pe lista.
# Maine trebuie lansata campania outdoor pe ecrane digitale care folosesc Raspberry Pi si ruleaza un cod Python
# pentru a afisa lista formatiilor.
#
# Putem crea o functie care sa faca modificarea in lista de mai jos, si care sa fie valabila cu orice alta lista
# de formatii, in cazul aceluiasi bug?
#
# ['Oigan + Doru', Vita de vie', 'The Mono Jacks', 'Robin and the backstabbers', 'Coma', 'Byron',
# 'Bogdan Simion & Lautarii de matase', 'Luna amara',
# 'Luiza Zan & Istvan Gyarfas', 'Piqued Jacks','Silent Strike', 'Amadeus',
# 'The Kryptonite Sparks', 'Toulouse Lautrec', 'EMIL', 'Dl Goe', 'BALTHAZAR']"""
# ['Oigan + Doru', 'Vita de vie', 'The Mono Jacks', 'Robin and the backstabbers', 'Coma', 'Byron',
# 'Bogdan Simion & Lautarii de matase', 'Luna amara',
# 'Luiza Zan & Istvan Gyarfas', 'Piqued Jacks','Silent Strike', 'Amadeus',
# 'The Kryptonite Sparks', 'Toulouse Lautrec', 'EMIL', 'Dl Goe', 'BALTHAZAR']

list = ['Oigan + Doru', 'Vita de vie', 'The Mono Jacks', 'Robin and the backstabbers', 'Coma', 'Byron',
        'Bogdan Simion & Lautarii de matase', 'Luna amara', 'Luiza Zan & Istvan Gyarfas', 'Piqued Jacks',
        'Silent Strike', 'Amadeus', 'The Kryptonite Sparks', 'Toulouse Lautrec', 'EMIL', 'Dl Goe', 'BALTHAZAR']

print(type(list))

print(dir(list))

# first_element = list[-1]
# print(first_element)
#
# last_element = list[0]
# print(last_element)
#
# list[0] = first_element
# print(list)
#
# list[-1] = last_element
# print(list)

list[0], list[-1] = list[-1], list[0]
print(list)