# - create a function taht given a string, returns the integer made from the string's digits. Given "0s1a3y5w7h9a2t4", the function should return th enumber of 1357924

def get_integer(string):
    number = ""
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in string:
            if i in nums:
                number += i
    return int(number)

x = get_integer("0s1a3y5w7h9a2t4")
print(x)
print(type(x))

# - create function clockHandAngles(seconds) that, given the number of seconds since 12:00:00, will print the angles ( in degrees ) of the hour, minute and second hands. 
# As a quick review, there are 360 degrees in a full arc rotation. Treat "straight-up" 12:00:00 as 0 degrees for all hands.

import math

def clockHandAngles(seconds):
    intervals = [720, 60, 1]
    degrees = []
    answer = {'Hour hand degrees:': 0, 'Minute hand degrees:': 0, 'Second hand degrees:': 0}
    index = 0

    #Calculate hours, minutes, seconds from seconds provided
    for time in intervals:
        degrees.append(math.floor(seconds / time))
        seconds = seconds % time

    #Update dictionary
    for key in answer.keys():
        answer[key] = degrees[index]
        index += 1

    #Print answer
    for key, value in answer.items():
        print(key, value)

clockHandAngles(6571)
