# import random
# import math



# print(round(random.random() * 51))
# the reason it's random.random is because we're importing random and the name of the module is random


# def bananas():
#     nanners = round(random.random() * 51)
#     if nanners % 2 == 0:
#         print(f"you have an even number of bananas {nanners}") 
# # we can use an f string here to embed variables within a string
#     return nanners

# bananas()
# the reason this returns a random # and none is because we haven't returned anything

# Dictionary Loops

weird_desserts = {
    "ted": "nanner pudding",
    "ice_cream": "Coffee ice cream",
    "milkshake": "soy sauce milkshake",
    "brownies": "black bean brownies",
    "tasty": False
}

# print(weird_desserts["ice_cream"])
# cannot do print(weird_desserts.ice_cream) because that's JS not Pyhon
# to add stuff to a dictionary, you just declare it out of thin air, essentially
weird_desserts["chocolate"] = "chocolate covered crickets"
#weird_desserts.pop("ice_cream")
#print(weird_desserts)

# .keys()
#print(weird_desserts.keys())
#for key in weird_desserts.keys():
    #print(key)
# print(weird_desserts.values())

# .items()
# print(weird_desserts.items())
for key, values in weird_desserts.items():
    print(key, ":", values)