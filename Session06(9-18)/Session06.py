#Conditional Statements
#In order to write useful programs, we need the ability to
#check conditions and change program behavior accordingly. 
#Conditional statements give us this ability

#Example 1
age = input('Please enter your age')

if int(age) >= 18:
    print('adult')
else:
    print('teenager') 

#Alternative Execution:
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else: # don't forget this colon 
    print('your age is', age)
    print('teenager')

#Topic 2: Chained Conditionals
#Elif is short for else if:

age = input('Please enter your age')

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')



