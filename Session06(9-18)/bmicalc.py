#Bmi defined

weight = input('Please enter your weight ')
height = input('Please enter your height ')
weight=float(weight)
height = float(weight)

bmi = 703 * (weight/ (height * height))

if bmi <= 18.5:
    print('underweight')
elif bmi < 18.5 and bmi <=25:
    print('normal weight')
elif 25 < bmi < 30:
    print('overweight')
else:
    print ('obese')

weight=float(weight)
height = float(weight)