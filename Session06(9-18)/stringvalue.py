#String Evaluator

def compare (varA, varB) :
    if isinstance(varA, str): 
        print('string involved')
    elif isinstance(varB, str): 
        print('string involved')
    else:
        if varA > varB:
            print('Bigger')
        if varA == varB:
            print('Smaller')
        else:
            print('smaller')
            
a = 'hello'
b = 3
c = 5

compare(a, b)
compare(b, c)