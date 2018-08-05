# Basics of Python function.

def function_name(parm1, parm2):
    return parm1 + parm2

print(function_name(5, 10))


# When you have multiple parameters and if one of those have default value, you have to
# define the parameter which have default value at last.
def function_name2(parm4, parm3=100):
    print(parm4)
    print(parm3)
    return parm3 + parm4

print(function_name2(100, 1000))


# Variables those defined outside of function, they are "global" variable.
# If you want to use that variable in a function, use "global" keyword within the function
# And manipulation against variable you refered with global keyword works only within that
# function.

parm5 = 100

def function_name3():
    global parm5
    print(parm5 + 1)

print(parm5)
function_name3()