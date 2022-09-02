# sweets = ["Vanilla", "strawberry chocolate", "rum & raisin", "pistachio", "Superman", "jolt cola", "code red"]
# print(sweets[:3])
# print(sweets[: :-7])
# print(sweets[:-1])
# new_list = sweets[:3]
# print(new_list)

# for sweet in sweets:
    # print(sweet)

# i = 0
# while i<= 5:
    # print(i)
    # i += 1

# for char in "Python":
    # print(char)

# sweets = ["Vanilla", "strawberry chocolate", "rum & raisin", "pistachio", "Superman", "jolt cola", "code red"]

# def add_sweets():
    # sweets.append("watchamacalit")
    #return sweets

#print(add_sweets())

def func_one():
    print(func_two())
    return "func 1"
def func_two():
    print(func_three())
    return "func 2"
def func_three():

    return "func 3"

print(func_one())