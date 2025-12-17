"""
Lists vs Tuples:

List: 
ordered, changeable, allows duplicate members., syntax [], methods are available, accessing the value is slow, data are not secured as compared to tuples

Tuple:
ordered, unchangeable, allows duplicate members. syntax (), methods are not available, accessing the value is fast, data are secured here than list

Set:
unordered, unchangeable, doesn't allow duplicate members, syntax {}, methods are available only for adding or removing data, 

Dictionary: 
ordered/unordered , changeable, doesn't allow duplicate members,  syntax = {}, methods are available 

"""

# car = {
    
#     "brand" : "toyota",
#     "color" : ["black","white","red"],
#     "model" : 2025,
#     "price" : 2000000

    
# }

# print(car)     

#Accessing the values from dictionary

# a = car["brand"]
# b = car["color"]

# a = car.get("brand")
# b = car.get("price")
# print(a)
# print(b)

# a = car.keys()
# print(a)
# b = car.values()
# print(b)


# Changing values of dictionary

# car["model"] = 2023
# car["price"] = 5000000
# print(car)

# using update() method to change the values of dictionary
# car = {
    
#     "brand" : "toyota",
#     "color" : ["black","white","red"],
#     "model" : 2025,
#     "price" : 2000000

    
# }

# car.update({"brand":"tesla", "model" : 2026, "color": ["black","white","red","blue","brown"]})
# car.update({"enginetype": "electric"})
# print(car)


# Removing data from dictionary:
# car = {
    
#     "brand" : "toyota",
#     "color" : ["black","white","red"],
#     "model" : 2025,
#     "price" : 2000000

    
# }

# using the pop() method to remove the specific item from dictionary
# car.pop("color")

#using popitem() method to remove the last inserted item from dictionary
# car.popitem()

# using del keyword to remove specific item from dictionary
# del car
# del car["model"]
# car.clear()
# print(car)

 # Iterating through dictionary
# car = {
    
#     "brand" : "toyota",
#     "color" : ["black","white","red"],
#     "model" : 2025,
#     "price" : 2000000

    
# }
# for i in car:
#     print(i)

# for i in car:
#     print(car[i])

# for i in car.keys():
#     print(i)

# for i in car.values():
#     print(i)

# for i,j in car.items():
#     print(i,j)


# Nested Dictionary


# car1 = {  "brand" : "toyota",  "color" : "black",  "model" : 2025,  "price" : 2000000 }
# car2 = {  "brand" : "tesla",  "color" : "white",  "model" : 2026,  "price" : 3000000 }
# car3 = {  "brand" : "bmw",  "color" : "red",  "model" : 2027,  "price" : 4000000 }

# cars = {"car1st": car1,"car2nd": car2,"car3rd": car3 }
# print(cars)


# cars = {
#     "car1": {  "brand" : "toyota",  "color" : "black",  "model" : 2025,  "price" : 2000000 },
#     "car2": {  "brand" : "tesla",  "color" : "white",  "model" : 2026,  "price" : 3000000 },
#     "car3": {  "brand" : "bmw",  "color" : "red",  "model" : 2027,  "price" : 4000000 }
# }


# print(cars)
# print(cars["car3"] ["brand"]
# print(cars["car3"] ["color"])


