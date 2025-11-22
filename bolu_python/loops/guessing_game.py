
SECRETE_NUMBER = 7

while True:    
    guess = int(input("Guess a Number between 1 to 12: "))

    if guess == SECRETE_NUMBER:
        print("You've won!")
        break
    else:
        print("Sorry, You are wrong!")

print("Thanks for playing!")
        