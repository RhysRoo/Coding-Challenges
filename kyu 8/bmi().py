def bmi(weight, height):
    x = weight / height ** 2
    if x <= 18.5:
        return "Underweight"
    elif x <= 25.0:
        return "Normal"
    elif x <= 30.0:
        return "Overweight"
    elif x > 30:
        return "Obese"
    
#codewars solution & my solution above ^^^^

# def bmi(weight, height):
#     b = weight / height ** 2
#     return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
    
if __name__ == '__main__':
    print(bmi(90, 3.0))