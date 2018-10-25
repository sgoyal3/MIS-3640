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

# # def no_e(word):
# #     for letter in word:
# #         if letter == 'e':
# #             return False
# #     return True

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

# print(has_no_e())

# def avoids(word, forbidden_letters):
#     for letter in word:
#         if letter in forbidden_letters:
#             return False
#     return True

# print(avoids('silly', 'a'))

# #import itertools
# #from itertools import chain, combinations
# #I tried to find all possible combinations of the planets string, but I couldn't seem to work it out


# def uses_only(word,letter_string):
#     for letter in word:
#         if letter not in letter_string:
#             return False
#     return True

# print(uses_only('silly', 'silly'))

def uses_all(word, req_letters):
    for letter in req_letters:
        if letter not in word:
            return False
    return True


# def uses_no_vowels():
#     fin = open('Session09/words.txt')
#     counter = 0
#     for line in fin:
#         word = line.strip()
#         if avoids(word, 'aeiouy'):
#             print(word)
#             counter += 1
#     return counter

# print(uses_no_vowels())

def uses_all_vowels():
    fin = open('Session09/words.txt')
    counter = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, 'aeiouy'):
            counter += 1
    return counter

print(uses_all_vowels())
        
def is_abecedarian(word):
    prior = word[0]
    for x in word:
        if x < prior:
            return False
        x = prior
    return True

is_abecedarian('silly')

#Exercise 2 
def is_abecedarian2(word):
    x = 0
    while x < len(word) - 1:
        if word[x] > word[x+1]:
            return False
        x = x + 1
    return True

is_abecedarian2('silly')

#The loop begins here at (x=0) and ends only when x -1 is last(compares second to last to last and then it ends)
#if next character is less than one being tested, we have break and function should return false

# #recursion
def is_abc_2(word):
    if len(word) < 2:
        return True
    if word[0] > word[1]:
        return False
    return is_abc_2(word[1])

is_abc_2('silly')

fin = open('Session09/words.txt')
line = repr(fin.readline())
line = fin.readline()

def is_abecedarians(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

def find_abc():
    fin = open('Session09/words.txt')
    counter = 0
    for line in fin:
        word = line.strip()
        if is_abecedarians(word):
            counter += 1
    return counter

print(find_abc())

def find_abc_longest():
    fin = open('Session09/words.txt')
    counter = 0
    currently_longest_word = ''
    for line in fin:
        word = line.strip()
        if is_abecedarians(word):
            counter += 1
            if len(word) > len(currently_longest_word):
                currently_longest_word = word
                print(word)
    return counter

print(find_abc_longest())