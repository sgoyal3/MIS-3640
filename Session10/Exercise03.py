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
    ret = []
    for x in t:
        total += x
        ret.append(total)
    return ret
t = [1 , 2, 3]
cumsum(t)

def middle(t):
    cut = t[1:] #stores all but first letter
    del(cut[-1]) #deletes last
    return cut
t = [1, 2, 3, 4]
middle(t)

def chop(t): #Isn't this the same thing?
    cut = t[1:] #stores all but first letter
    del(cut[-1]) #deletes last
    return cut

def is_sorted(t): #Indexes and sorts
    for i in range(len(t)-1): 
        if t[i+1] < t[i]:
          return False 
    return True
is_sorted([1, 2, 2])

def is_anagram(word1, word2):
    x1 = list(word1)
    x2 = list(word2)
    x1.sort()
    x2.sort()
    if x1 == x2:
        return True

is_anagram('stop', 'pots')
is_anagram([1, 2, 2], [2, 1, 2])

def has_duplicates(s):
    t=0
    for x in s:
        for y in s:
            if x == y:
                t = t+1
    if t > len(s):
        return True

def has_duplicates_2(s):
    for x in s:
        if s.count(x) > 1:
            return True
    return False

print(has_duplicates_2('abcc'))




def has_adj_dupl(s):
    x = list(s)
    for i in x:
        if str(s) == str(s-1):
            return True
        else:
            return False


print(has_adj_dupl('cba'))
print(has_adj_dupl('abca'))
print(has_adj_dupl('abbc'))



t = [3, 1, 2]
t2 = t[:]
t2.sort()
t2

t