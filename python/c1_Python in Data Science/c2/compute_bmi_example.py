def compute_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'
    return result


input_weight = int(input('weight = '))
input_height = float(input('height = '))

print(compute_bmi(input_weight, input_height))
