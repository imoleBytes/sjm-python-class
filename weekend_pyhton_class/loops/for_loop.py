
# print("**start**")

# for name in ["Jide","Paul","Nurein","Ade"]:
#     if len(name) == 6:
#         break
#     print(name)

# print("**end**")

# for num in range(2,10,2):
#     print(num)
SECRETE_NUMBER = "7"
print("Welcome to Guesing Game")
name = input("Enter your Name: ")
print(f"Welcome, {name}")

for i in range(3):    
    guess = input("Guess a number between 1-10: ")

    if guess == SECRETE_NUMBER: 
        print("CORRECT!!, YOU WIN")
        break
    else:
        print("Sorry, you FAIL!")
        if i == 2:
            print("You have exhausted your chances!")

print("Thank you for playing")