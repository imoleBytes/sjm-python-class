
# <   less than
# >     greater than
# <=    less than or equal to 
# >=    greater than or equal to 
# ==    eqauls to

# 21 <= 20

print("=======================================")
print("=======================================")
print("===== Welcome To Our Guessing Game ====")
print("=======================================")
print("=======================================")

points = 0

name = input("Please, state your Name: ")


age = int(input("What is your age: "))
if age < 18:
    print(f"Sorry, {name} you are underage")
    print(f"Come back in {18 - age} years!")
else:


    guess = input("Choose a number between 1-10: ")

    if guess == "6":
        print("Hurray!!,you got it right")
        points = points + 1
        print("Weldone, "+name)

    else:
        print("oops, Youre wrong. Try again later!")

    print(f"Your points is {points}!")