print('''Body mass index, or BMI, is a way to help you figure out if you are at a healthy weight for your height or not. 
BMI is a number based on your weight and height.\n''')

print('''Underweight: BMI is less than 18.5
Normal weight: BMI is 18.5 to 24.9
Overweight: BMI is 25 to 29.9
Obese: BMI is 30 or more\n''')

print('**********THE BMI CALCULATOR**********\n')

w=float(input("enter your weight in kg\n"))
h=float(input("enter your height in metres\n"))
bmi=(w/(h*h))
print("Your BODY MASS INDEX is:",round(bmi,1),'\n')

if(bmi<18.5):
    print('You are UNDERWEIGHT')
if(bmi>=18.5 and bmi<25):
    print('Your weight is NORMAL')
if(bmi>=25 and bmi<30):
    print('You are OVERWEIGHT')
if(bmi>=30):
    print('You are OBESE')

c=input("\n\nPress enter to exit")
