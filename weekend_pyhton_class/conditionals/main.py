# print("Welcome to Weather APP")

# weather = "SUUNNY"

# if weather.lower() == "rainy":
#     print("oops, it is rainy, take your umbrella")
# elif weather.lower() == "sunny":
#     print("the weather is sunny")
# elif weather.lower() == "cloudy":
#     print("it is cloudy")
# else:
#     print("Hurray! the weather is clear, have a nice day")

# print("Thank you for using our App")


"""
CREATE A GRADE SYSTEM THAT COLLECT  A GRADE AND SAYS ITS REMARK
A > Excellent
B > Very Good
C > Good
D > Fair
E > Pass
F > Fail
others Invalid grade

This program shout be able to collect grade and says its corresponding remark

e.g if the person enter A, it hould say Excellent, if B it should say Very Good, 
if not any of the grade iit should say Invalid grade
"""

while True:
    student_grade = input("Enter Your grade: ")

    if student_grade == "A":
        print("Result, Excellent")
    elif student_grade == "B":
        print("Result, Very Good")
    elif student_grade == "C":
        print("Result, Good")
    elif student_grade == "D":
        print("Result,Fair")
    elif student_grade == "E":
        print("Reul,Pass")
    elif student_grade == "F":
        print("Result,Fail")
    else:
        print("Invalid grade")
print("Thanks for using this grading system")



