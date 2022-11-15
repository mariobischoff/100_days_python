# Body Mass Index Calculation 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2

bmi_message = ''

if bmi < 18.5:
    bmi_message = "underweight"
elif bmi < 25:
    bmi_message = "normal weight"
elif bmi < 30:
    bmi_message = "overweight"
elif bmi < 35:
    bmi_message = "obese"
else:
    bmi_message = "clinically obese"

print(f"Your BMI is {bmi:.2f}, you are {bmi_message}.")
