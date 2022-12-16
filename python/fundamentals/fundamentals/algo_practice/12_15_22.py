# - create a function that, given an input string, returns a boolean whether parenteses in that string are valid. given input "y(3(p)p(3)r)s", returns true.
#     given "n(0(p)3", return false. given "n)0(t(0)k", return false

def true_or_false(string):
    open = 0
    close = 0
    for x in string:
        if close > open:
            return False
        if x == "(":
            open += 1
        elif x == ")":
            close += 1
    if open == close:
        return True
    return False


print(true_or_false("y(3(p)p(3)r)s"))
print(true_or_false("n(0(p)3"))
print(true_or_false("n)0(t(0)k"))