person = {
     "name": "Alex",
     "age": 18,
     "gender": "male"
     }
print(person["age"])


cars = ("bmw", "reno", "lada")

cars2 = ["mesedes", "kia"]

cars2.append("honda")

hours = 17

if hours > 5 and hours <= 12:
    print("утро")
elif hours > 12 and hours <= 18:
    print("день")
elif hours > 18 and hours <= 23:
    print("вечер")
elif hours > 23 or hours <= 5:
    print("ночь")



string = "арбуз, дыня, яблоко, апельсин, банан"


def fruits(fruits_str):
    list_fruits = string.split(", ")
    return list_fruits[0], list_fruits[-1]


fruit1, fruit2 = fruits(string)

print(fruit2)
