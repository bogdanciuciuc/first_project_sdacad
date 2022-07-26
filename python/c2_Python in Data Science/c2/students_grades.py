math_grades = {'Andreea': 10,
               'Ionel': 7,
               'Eva': 8,
               'Mitica': 7,
               'Gabi': 5,
               'Alin': 10,
               'Alice': 6,
               'Cristi': 9,
               'Corina': 8,
               'Mihai': 5,
               'Anca': 7,
               'Teodor': 5,
               'Maria': 8,
               'Gustav': 7,
               'Ionela': 10}

grade_list = list(math_grades.values())
average = int(sum(grade_list) / len(grade_list))

over_average = 0
under_average = 0
for _, key in math_grades.items():
    if key > average:
        over_average += 1
    elif key<average:
        under_average +=1

print(f'{over_average} students over average and {under_average} under average')
