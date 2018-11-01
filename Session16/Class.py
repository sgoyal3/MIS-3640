class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

time = Time()
time.hour = 1
time.minute = 31
time.second = 30

#Exercise 1: Write a function called print_time that takes
#a Time object & prints it in the form hour:minute:second. 
# Hint: '{:02d}'.format() prints an integer using at least two digits, 
# including a leading zero if necessary.

def print_time(time):
    
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

print_time(time)
    
    
#Exercise 2: boolean function called is_after that takes two Time objects, t1 and t2, 
#and returns True if t1 follows t2 chronologically and False otherwise. 
#Challenge: don’t use an if statement.

def is_after(t1, t2):
    if t1.hour > t2.hour:
        return True
    elif t1.hour == t2.hour:
        if t1.minute > t2.minute:
            return True
        elif t1.minute == t2.minute:
            return t1.second > t2.second
        else:
            return False
    else:
        return False
         
time2 = Time()
time2.hour = 3
time2.minute = 12
time2.second = 14

print_time(time2)

print(is_after(time,time2))

def is_after2 (t1,t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
    
print(is_after2(time,time2))

#Exercise 2: Improve Add Time

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

print(add_time(time,time2))

# #Exercise 3: Improve increment that creates new time object
# def increment(time, second):
#     """Adds seconds to a Time object."""
#     time.second += second

#     if time.second >= 60:
#         time.second -= 60
#         time.minute += 1

#     if time.minute >= 60:
#         time.minute -= 60
#         time.hour += 1

# def increment_2(time, second):
#     """return a Time object after incrementing"""
#     time.second += second
#     sum = Time()
#     sum.hour = time.hour
#     sum.minute = time.minute
#     sum.second = time.second + time.second

#     while time.second >= 60:
#         time.second = time.second - 60
#         time.minute = time.minute + 1

#     while time.minute >= 60:
#         time.minute = time.minute - 60
#         time.hour = time.hour + 1
    
#     return sum
    
# second = Time()
# second.hour = 0
# second.minute = 0
# second.second = 74

# print(increment_2(time2, second))

#Designed Development:
 
def time_to_int(time):
    """Computes the number of seconds since midnight.
    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time_2(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


""""""""""""""""""""""""""""""""""""
# Exercise 4
""""""""""""""""""""""""""""""""""""


def substract_time(t1, t2):
    """Substracts two time objects.
    t1, t2: Time
    returns: Time
    """
    

""""""""""""""""""""""""""""""""""""
# Error handling
""""""""""""""""""""""""""""""""""""


def valid_time(time):
    """Checks whether a Time object satisfies the invariants.
    time: Time
    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_time2(t1, t2):
    """Adds two time objects.
    t1, t2: Time
    returns: Time
    """
    # assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

# done = add_time2(start, duration)
# print_time(done)


# Exercise 5: Mult-time

def mul_time(t1, factor):
    """Multiplies a Time object by a factor."""
    assert valid_time(t1)
    seconds = time_to_int(t1) * factor
    return int_to_time(seconds)

print_time(mul_time(time, 3))