class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """
    
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.
        hour: int
        minute: int
        second: int or float
        """
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)
        
    def print_time(self):
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second))
        
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.
        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
        
    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True

    
    def increment(self, seconds):
        result = Time()
        result.hour, result.minute, result.second = self.hour, self.minute, self.second
        result.second += seconds

        if result.second >= 60:
            result.second -= 60
            result.minute += 1

        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1
        return result
        
    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

# Two ways to call:
Time.print_time(start)
start.print_time()

# Two ways to call:
Time.print_time(start)
start.print_time()



start.hour = 15
start.minute = 18
start.second = 50

start.print_time()
print(start.time_to_int())

end = start.increment(30)
# end.print_time()
print(end.is_after(start))

traffic = Time(0, 30, 0)
print(traffic)

expected_time = Time(10, 15, 0)

traffic.print_time()
expected_time.print_time()
# print(start.is_as_expected(traffic, expected_time))

default_time = Time()
default_time.print_time()