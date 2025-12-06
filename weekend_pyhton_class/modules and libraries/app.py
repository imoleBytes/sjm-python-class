import sys
import library.mymath as mymath
args = sys.argv

if len(args) != 4:
    print("invalid usage")
    print("app.py [add | mul | div | sub | pow] num1 num2")
    exit()
operation = args[1]
a = float(args[2])
b = float(args[3])

res = None
if operation == "add":
    res = mymath.add(a, b)
elif operation == "sub":
    res = mymath.sub(a, b)
elif operation == "mul":
    res= mymath.mul(a, b)
elif operation == "div":
    res = mymath.div(a, b)
elif operation == "pow":
    res = mymath.pow(a, b)
else:
    print("invalid operation (add,mul,div,sub,pow)")
    exit()


print(f"The answer is {res}")