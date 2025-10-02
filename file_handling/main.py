print("***start***")

f = open("students.txt")

list_of_students = []

content =f.readlines()
for line in content:
    name = line.rstrip("\n").split(",")[0]
    course = line.rstrip("\n").split(",")[1]
    age = line.rstrip("\n").split(",")[2]

    student = {"name": name, "course": course, "age":age}
    list_of_students.append(student)

    # print(f"Student: {name} and age is: {age}")

# cont = content.rstrip("\n").split(",")
# print(cont[0])

f.close()

sum = 0
for i in list_of_students:
    sum += int(i["age"])

average = sum/len(list_of_students)

print(f"The average age is: {average:.2f}")

# print(list_of_students[1]["age"])
print("***end****")