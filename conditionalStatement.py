# Conditional Statement -> logic checking

# if statement   if
# else if statement  elif 
# else statement  else 


#Indentation

# age = int(input("Enter you age please:"))
# if age >= 18 :
#     print("You can vote")
# else:
#     print("You cannot vote")


# number = int(input("Enter any number:"))
# if number % 2 == 0: 
#     print(f" {number} is an even number")  
# else:
#     print(f" {number} is an odd number")
    
  
  
    
# Nested if-else conditions

# number = -21
# if number >= 0:
#     if number % 2 == 0:
#         print("Postive even number")
#     else:
#         print("Positive odd number")  
# else:
#     print("Negative number")


# LOgical operators -> and, or, not
percentage = 50
if percentage >= 90 and percentage <= 100:  #and operator -> and operator ko dubai patti side ko conditions satisfy hunu parxa
    print("A+ grade")   
elif percentage  >= 80 and percentage < 90:
    print("A grade")   
elif percentage >= 70 and percentage < 80:
    print("B+ grade")   
elif percentage >= 60 and percentage < 70:
    print("B grade")
else:
    print("Fail")
    
#  or -> Or operator kunai auta conditions satisfy bhayo bhane hunxa

age = int(input("Enter your age:"))
if age > 18 or age == 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
    
