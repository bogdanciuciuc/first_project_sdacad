list = ['Oigan + Doru', 'Vita de vie', 'The Mono Jacks', 'Robin and the backstabbers', 'Coma', 'Byron',
        'Bogdan Simion & Lautarii de matase', 'Luna amara',
        'Luiza Zan & Istvan Gyarfas', 'Piqued Jacks','Silent Strike', 'Amadeus',
        'The Kryptonite Sparks', 'Toulouse Lautrec', 'EMIL', 'Dl Goe', 'BALTHAZAR']

def index_transformation(list):
        list [0], list[-1] = list[-1], list[0]
        return list


index_transformation(list)
print(list)

list_2023 = ['Metallica', 'Slipknot', 'Megadeth']
index_transformation(list_2023)
print(list_2023)
