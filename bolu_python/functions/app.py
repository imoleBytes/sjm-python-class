


# def greet(name="John Doe", age=20):
#     return f"Hi, {name}. You are {age} years old"    

# msg = greet(age=28)
# print(msg)

# SCOPE

# GLOBAL SCOPE
# LOCAL SCOPE

name = "Imole"


def greet():
    age = 12
    print(f"Hi, {name}. You are {age} years old")
    
greet()


print(age)