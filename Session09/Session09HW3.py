#Exercise 3
fin = open('Session09/words.txt')

line = repr(fin.readline())
line = fin.readline()

#Since we need at least six letters, we can exclude all shorter than that
#Apparently brackets are used for dictionaries and lists, which I didn't know, so
#some prior code might have parenthesis that need to be replaced

def three_con(word):
    x = 0
    count = 0
    while x < len(word) - 1:
        if word[x] == word[x+1]:
            count = count + 1
            if count == 3:
                print(word)

            
#Explained: while x is less than the length of the word - 1, and as long as x = the letter directly after it,
#and as long as this occurs three times, then we get a printing of the words that have three consec. double letters
#Don't know why my code won't run though, and produce the correct letters, got kinda lost here

def sixer():    
    for line in fin:
        word = line.strip()
        if three_con(word):
            print(word) 
sixer()

        

