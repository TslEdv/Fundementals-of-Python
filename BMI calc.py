def weight(bmi):
    if bmi >= 30:
        print("Obesity!")
        return
    elif (bmi >= 25) and (bmi<=29.9):
        print("Overweight!")
        return
    elif (bmi >= 18.5) and (bmi<=24.9):
        print("Normal weight!")
        return
    else:
        print("Underweight!")
        return
bmi = float(input("Your BMI: "))
weight(bmi)