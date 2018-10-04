#Lists

#Creating New Lists:
[10, 20, 30, 40]
# The elements of a list don’t have to be the same type. 
# A list within another list is nested. 
['spam', 2.0, 5, [10, 20]] 
AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
print(AFC_east, numbers, empty)

#Lists are Mutable:

#Syntax for accessing elements is same as accesing string, use brackets
AFC_east[3] = 'New York Giants'
print(AFC_east)

#Strings are Immutable

#Transversing a List:
AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
for team in AFC_east:
    print(team)

#List Operations
a = [10,11,12]
b = [13,14,15]
c = a + b
print(c)

['Tom Brady', 'Bill Belichick']*3

#List Slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
print(t[1:4])
print(t[1:6])

#List MEthods & Exercise 2(Reading Documentation)
#Played Around with Various Methods


















