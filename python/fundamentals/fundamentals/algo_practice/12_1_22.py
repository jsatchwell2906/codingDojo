# Threes and Fives
#         Write a function threesFives() that adds each value from 100 to 4000000 (inclusive) if that value is evenly divisible by 3 or 5 but not both.
#         display the final sum in the console

def threes_and_fives():
    sum = 0
    for i in range (100,4000001):
        if i % 3 == 0 and i % 5 == 0:
            pass
        elif i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum        


print(threes_and_fives())


# Sum to One Digit
#       Write a function sumToOne(num) that gven a number sums that number's digits repeatedl until the sum is only one digit. Return that final one digit result.
#       SumToOne(18) would return 9

def sum_to_one(num):
    str_num = str(num)
    for i in range(len(str_num) - 1):
        if((int(str_num[i])+int(str_num[i+1])<10) and (int(str_num[i])+int(str_num[i+1]) >=-9 )):
            return int(str_num[i]) + int(str_num[i + 1])
    return "no 2 numbers in this number make a single digit number"

    str_num = str(num)
    sum = num
    while sum >= 10:
        for i in range(len(str_num) - 1):
            if sum >= 10:
                sum = int(str_num[i]) + int(str_num[i + 1])
    return sum

    # for i in str_num:
    #     sum += int(i)
    # return sum

print(sum_to_one(937))
