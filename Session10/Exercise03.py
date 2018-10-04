#Exercise 03

#Nested Sum:

def nested_sum(t):
    total = 0
    for x in t:
        for element in x:
            total += element
    return total

t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)

def cumsum(t):
    total = 0
    for x in t:
        total += x
    return cumsum

def middle(t):
    cut = t[1:] #stores all but first letter
    del(cut[-1]) #deletes last
    return cut

def chop(t): #Isn't this the same thing?
    cut = t[1:] #stores all but first letter
    del(cut[-1]) #deletes last
    return cut

def is_sorted(t): #Indexes and sorts
    for i in range(len(t)-1): 
        if t[i+1] < t[i]:
          return False 
    return True


def is_anagram(word1, word2):
    x1 = list(word1)
    x2 = list(word2)
    x1.sort()
    x2.sort()
    if x1 == x2:
        return True

is_anagram('stop', 'pots')

def has_duplicates(s):
    t=0
    for x in s:
        for y in s:
            if x == y:
                t = t+1
    if t > len(s):
        return True





