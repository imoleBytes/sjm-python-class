print("== Weather Game ==")


weather = input("Update Weather (rainy,sunny,clear): ").lower().strip()

if weather == "rainy": # "  rainy  " == "rainy"
    print("it is rainy, Go out with umbrela")
elif weather == "sunny":
    print("it is sunny o, if you must go out, do so with sunshade")
elif weather == "clear":
    print("Nice weather")
else:
    print("invalid weather value. Be Responsible")

