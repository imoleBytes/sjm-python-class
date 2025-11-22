
# print("start")
# try:
#     print(x)
    
# except:
#     print("variable x not found")

# print("end")

def divide():
    res = 0
    
    try:        
        num_a = int(input("Enter first number: "))
        numb_b = int(input("Enter Second number: "))
        print(md)
        res = num_a / numb_b
        print(f"The result is {res}")
    except ValueError:
        print("please enter valid number")
    except ZeroDivisionError:
        print("cannot divide by zero")
    except NameError:
        print("name error occured")
    except:
        print("there's an error")

divide()

print("Thank you for using my division calculator!")