def bmi_calculator():

    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    height = height / 100
    BMI = weight / (height * height)

    print(f"Your Body Mass Index is: {BMI:.2f}")

    if BMI > 0:

        if BMI <= 16:
            print("You are severely underweight")

        elif BMI <= 18.5:
            print("You are underweight")
