# numbers = [1,2,3,4,5,6,7,8,9,10]

# square_list = [i**2 for i in numbers]
# cube_list = [i**3 for i in numbers]

# print(square_list)
# print(cube_list)


# even_numbers = [i for i in numbers if i%2 == 0]
# odd_numbers = [i for i in numbers if i%2 != 0]
       
        
# print(even_numbers)
# print(odd_numbers)

# numbers = [1,2,-4,-7,6,9,-9,5]
# newlist = [i for i in numbers if i>=0]
# newlist.sort(reverse=True)
# print(newlist)


# birds = ["sParrow", "eaGle", "parrOt", "Pigeon", "peacocK", "oWl"]

# newlist = [i.upper() for i in birds]
# newlist2 = [i.lower() for i in newlist]

# print(newlist)
# print(newlist2)

animals = ["dog", "cat", "parrot", "rabbit", "fish", "lion","dinosaur"]

# new_list = [i for i in animals if i.startswith("r")]
# print(new_list)

# for i in animals:
#     if i.startswith("d"):
#         print(i)

# for i in animals:
#     length = len(i)
#     print(length)

lenght_list = [len(i) for i in animals]
print(lenght_list)