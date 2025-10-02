print("=== Welcome To Guessing Game ===")
print("================================")

name = input("State your Name: ")
age = int(input("Your Age: "))

if age < 18:
    print("You are underage.")
else:
    guess = int(input("Guess a number betwween 1 - 10: "))
    
    if guess == 7:
        print(f"Hurray! {name}, You got it right. The magic number is 7.")
    else:
        print("Sorry Looser! Try again")

print("The END")