bob_age = 30
sarah_age = 28
mary_age = 50


if bob_age > sarah_age:
    print("Bob is older than Sarah")
    if bob_age > mary_age:
        print("Bob is the oldest")

if bob_age > sarah_age or bob_age > mary_age:
    print("Bob is older than Sarah")
    print("Bob is the oldest")


"""
The AND LOGICAL OPERATOR
X   Y   X AND Y
T   T   T
T   F   F
F   T   F
F   F   F     
"""