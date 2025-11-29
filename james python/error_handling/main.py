# print("A")
# print("B")
# print("C")
# try:
#     print(D)
    

# except:
#     print("there was an error")

# print("E")
# print("F")

# try:
#     print(x)
# except:
#     print("an error")

# arr = ["a", "b", "c"]
# try:
#     el = arr["er"]
# except NameError:
#     print("sorry, name errror")
# except ValueError:
#     print("sorry, value errror")

# except IndexError:
#     print("sorry, na index errror bitch")
# except Exception as e:
#     print("there was an error: ", e)



x = 32
y = 0

if y ==0:
    raise ValueError("sorry o y, should not be zero")

z = x / y

print(z)


"""
BUILD A SIMPLE COMMAND LINE BANKING SYSTEM WHERE A USER CAN:
    - Create an account
    - Deposit money
    - Withdraw money
    - Check balance
    - Quit the program
The program must handle errors gracefully
"""