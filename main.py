def bmi_calculator():

    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    height = height / 100
    BMI = weight / (height * height)
