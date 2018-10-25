# names = ['Defne', 'Jack', 'Angela']
# scores = [95, 75, 85]

# #Q. Given a student's name, how do we find their grades?
# #Better way to show key-value relationship is dictionar:

# """A dictionary contain a collection of indices.
#    which are called keys, and a collection of values.
#    Called a key-value pair."""
   
# grades = dict()
# print(grades)

# grades['Defne'] = 90
# #creates an item that maps from the key Defne to value 90.
# print(grades)

# grades ={'Defne': 90, 'Jack': 75, 'Angela': 85}
# print(grades)

# print(grades['Jack'])

# print(len(grades))
# #returns 3

# 'Jack' in grades 
# #checks only the keys
# #returns true

# 90 in grades.values() 
# #checks the values

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d

# h = histogram('Bookkeeper')
# print(h)
# Dictionaries have a method called get that takes a key and a default 
# value. If the key appears in the dictionary, get 
# returns the corresponding value; otherwise it returns the 
# default value. For example:

# number_of_e = h.get('e', 0)
# number_of_a = h.get('a', 0)
# print(number_of_e)
# print(number_of_a)

#Rewrite histogram using get

def histogram2(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(s, 0)
    return d
print(histogram2('Bookkeeper'))

        











