# #Exercise 1
fin = open('Session09/words.txt')

line = repr(fin.readline())
line = fin.readline()

# counter = 0
# for line in fin:
#     word = line.strip()
#     counter += 1

# # print(word)
# print(counter)

# def word_finder():
#     for line in fin:
#         word = line.strip()
#         if len(word) > 20:
#             print(word)

# word_finder()

# def no_e(word):
#     for letter in word:
#         if letter == 'e':
#             return False
#     return True

# def has_no_e():
#     num_of_words = 0
#     count = 0
#     for line in fin:
#         num_of_words = num_of_words + 1
#         words = line.strip()
#         if words.find("e") == -1:
#             print(words)
#             count = count + 1
#     percent = (count/num_of_words) * 100
#     print("Percent:", percent)

# def avoids(word, forbidden_letters):
#     for letter in word:
#         if letter in forbidden_letters:
#             return False
#         else:
#             return True

#import itertools
#from itertools import chain, combinations
#I tried to find all possible combinations of the planets string, but I couldn't seem to work it out


# def uses_only(word,letter_string):
#     for letter in word:
#         if letter not in letter_string:
#             return False
#     return True

# def uses_all(word, req_letters):
#     for letter in word:
#         if letter not in word:
#             return False
#     return True

# def is_abecedarian(word):
#     prior = word(0)
#     for x in word:
#         if x < prior:
#             return False
#         x = prior
#     return True

#Exercise 2
#while 
# def is_abecedarian(word):
#     x = 0
#     while x < len(word) - 1:
#         if word[x] > word[x+1]:
#             return False
#         x = x + 1
#     return True

#The loop begins here at (x=0) and ends only when x -1 is last(compares second to last to last and then it ends)
#if next character is less than one being tested, we have break and function should return false

#recursion
def is_abc_2(word):
    if len(word) < 2:
        return True
    if word[0] > word[1]:
        return False
    return is_abc_2(word[1])

