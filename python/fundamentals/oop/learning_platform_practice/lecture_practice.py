"""
    Write a function that accepts a list of numbers and returns the sum of all the even numbers that follow an odd number.
"""

def add_evens_after_odds(data):

    sum = 0

    last_value_is_even = False

    for value in data:

        if value % 2 == 0 and last_value_is_even == True:
            sum += value

        last_value_is_even = value % 2
        
    return sum

print ( 'test 1: ', 'pass' if add_evens_after_odds([1, 2, 3, 4]) == 6 else 'fail' )
print ( 'test 2: ', 'pass' if add_evens_after_odds([6, 9, 8, 4]) == 8 else 'fail' )

# add 2 tests of your own
