
def print_hist(data):
    for x in sorted(data):
        g = data[x]
        print(x,': ',g*'*')
        
    '''given a dictionary of letter: positive integer pairs, 
    print rows with the letter and a number of asterisks equal
    to the positive integer. The rows should be printed in key order.
    No return is required.
    data: a dictionary of letter: positive integer pairs
    Example:
    letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
    print_hist(letter_counts)
    Expected output:
    A: ***
    B: **********
    C: ******
    Z: ********
    '''
letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
print(print_hist(letter_counts))