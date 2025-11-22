# 

# def my_function(name, age):
#     print(f"Hello {name}, you are {age} years old")
    
# my_function("Quadri")


# def greet(age, name="World"):
#     print(f"Hi {name}, you are {age} years old")
    
    
# greet(21, "imole")
# greet(12)


# def greetAllStudents(students):
#     for name in students:
#         print(f"Hi {name}")
        
        
        

# people = ["Jide", "Nuru", "Habeeba"]

# greetAllStudents(23)


def doubleTheNumber(num=10):
    result = 2 * num
    return result

# answer = doubleTheNumber(15)


def getGrade(score):
    grd = "" 
    if score >= 70:
        grd = "A"
    elif score >= 60:
        grd = "B"
    elif score >= 50:
        grd  = "C"
    elif score >= 45:
        grd = "D"
    elif score >= 40:
        grd = "E"
    else:
        grd = "F"
    return grd
    
        


grade = getGrade(23)
print(grade)