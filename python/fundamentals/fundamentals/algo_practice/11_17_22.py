# Write a function that given an amount of cents returns the fewest number of quarters, dimes, nickels, and pennies required to equal that amount.
#         coinCalculator(99) should return {"Quarters":3,"Dimes":2,"Nickels":0,"Pennies":4}
# import math
def coinCalculator(cents):
    change = {
        'quarters': 0, 
        'dimes': 0, 
        'nickels': 0, 
        'pennies': 0
    }

    while cents > 0:
        if cents >= 25:
            change['quarters'] += 1
            cents -= 25

        elif cents >= 10:
            change['dimes'] += 1
            cents -= 10

        elif cents >= 5:
            change['nickels'] += 1
            cents -= 5

        elif cents >= 1:
            change['pennies'] += 1
            cents -= 1

    # if cents >= 25:
    #     change['quarters'] = math.floor(cents/25)
    #     cents -= (change["quarters"] * 25)
    # if cents >= 10:
    #     change['dimes'] = math.floor(cents/10)
    #     cents -= (change["dimes"] * 10)
    # if cents >= 5:
    #     change['nickels'] = math.floor(cents/5)
    #     cents -= (change["nickels"] * 5)
    # if cents >= 1:
    #     change['pennies'] = math.floor(cents/1)
    #     cents -= (change["pennies"] * 1)

    return change 
print(coinCalculator(99))


#     Bonus:
#         Account for Dollar increments as well (Ones/Fives/Tens/Twenties/Fifties/Hundreds)
#     Double Bonus:
#         Account for the elusive 2 dollar bills as well.

