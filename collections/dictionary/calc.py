import math

def addition(x,y):
    total = x + y
    return total

def subtraction(x,y):
    total = x - y
    return total

def square_root(num):
    val = math.sqrt(num)
    return val

# ****************************
# DO NOT TOUCH BELOW THIS LINE
# ****************************
# x = addition(20,5)
# y = subtraction(10,4)
# z = square_root(81)



# if x == 25 and y == 6 and z == 9 or z == 9.0:
#     print("Correct")

def isCapital(word):
    return word.isupper()

res = isCapital("asdfghj")

print(res)