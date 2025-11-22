
# num  = 0

# while num < 10:
#     print(num)
#     # num = num + 1
#     num += 1
#     if num == 8:
#         break
    
    
# print("End")

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

while start <= end: 
    if start % 2 == 0:
        print(start)
    start += 1