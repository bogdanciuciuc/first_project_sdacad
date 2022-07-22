# declare function
def compute_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'
    return result


# call function
print(compute_bmi(115, 1.80))
