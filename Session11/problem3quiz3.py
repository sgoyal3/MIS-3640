def is_increasing(data):
    '''
    Return True if the list is currently sorted in increasing order.
    '''
    for n in range(len(data) + 1):
        if data[n] >= data[n+1]:
            return False
        else:
            if data[n] < data[n+1]:
                return True

# Uncomment the following lines to test
data_1 = [10, 11, 2018]
data_2 = [11, 10, 2018]
data_3 = [10, 10, 2018]
print(is_increasing(data_1))
print(is_increasing(data_2))
print(is_increasing(data_3))

# Expected output:
# True
# False
# False
