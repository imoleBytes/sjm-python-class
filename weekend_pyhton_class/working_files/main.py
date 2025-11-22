

# f = open("humpty_poem.txt", "r")
# content = f.read()
# f.close()
# print(content)



""" ASSIGNMENT
- Create a function Called readPoem with optional argument n
- when called like this readPoem(), it should print all the lines 
-   of the poem
- but when called with the argument like readPoem(3), it should
-   print only the line of the poem that match the number
"""



f = open("humpty_poem.txt", "r")
content = f.readlines()

f.close()
print(content[3])
