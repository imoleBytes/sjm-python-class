
# Dictionary

car = {
    "name": "camry", 
    "brand": "toyota", 
    "price": 12000.50, 
    "color": "black"
}
print(car)
# car["price"] = 50000
# car["brand"] = "honda"
# car["name"] = "accord"

car["owner"] = "Clinton Ajanlekoko"


car2 = car.copy()

# car2.clear()

print(car.get("owner","government"))


# print(car["color"])
# print(car)
# print(car2)
