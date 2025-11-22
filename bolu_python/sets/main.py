# sets is a collection which is unordered

# setA = {"a", "b", "c", "e","x", "y", "z"}
# setB = {"b", "d", "e"}
# setD = {"x", "z"}

# setA.

# setA.remove("m")
# print(setA)

# print(setB.difference(setA))

# print(setD.issubset(setA))
# print(setD.issuperset(setA))

# setC = setA.union(setB)/
# setC = setA.intersection(setB)
# print(setC)

# set1.add("a")

# val = set1.pop()
# print(val)
# print(set1)

# assignment

math = {"Jide", "Quadri","Clinton", "Collins", "Bayo"}
physics = {"Korede", "Goodluck", "Temi","Quadri", "Jide"}
biology = {"Praise","Jide", "Collins", "Feyi", "Korede"}

"""
SHOW
    1. A is students taking both Math and physics
    2. B is students taking either Math or physics
    3. C students taking Math but not phyics
    4. D student taking Math and Physics but not biology
"""

A  = math.intersection(physics)
print(A)
B = math.union(physics)
print(B)

C = math.difference(physics)
print(C)

D = math.intersection(physics).difference(biology)
print(D)
# print(set1[0])