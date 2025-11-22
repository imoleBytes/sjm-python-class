def getgradePoint(grade):
    if grade == "A":
        return 5
    elif grade == "B":
        return 4
    elif grade == "C":
        return 3
    elif grade == "D":
        return 2
    elif grade == "E":
        return 1
    else:
        return 0
    
def calculateCGPA(data):
    total_points = 0
    total_units = 0
    
    for i in data:
        points = getgradePoint(i["grade"]) * i["unit"]
        total_points = total_points + points
        total_units += i["unit"]
    
    cgpa = total_points/total_units
    
    return float(f"{cgpa:.2f}")
    
##########################
# DO NOT TOUCH BELOW
student_result = [
    {"course": "eng", "grade": "A", "unit": 2},
    {"course": "math", "grade": "A", "unit": 3},
    {"course": "phy", "grade": "A", "unit": 2},
    {"course": "chm", "grade": "B", "unit": 4},
    {"course": "csc", "grade": "A", "unit": 3}
]
cgpa = calculateCGPA(student_result)

print(f"The student CGPA is {cgpa}")

"""
Create a function called 'calculateCGPA'
Thi function should collect a single argument of type 
list of dictionary and return the CGPA

Note:   A == 5, B == 4, C == 3, D == 2, E == 1, F == 0
"""