

# b = bool(int(input("bool: ")))
# print(b)
# print(type(b))


f = open("db.csv")

while True:
    ln = f.readline()
    if ln == "":
        break
    print(ln, "m", end="")
    

f.close()