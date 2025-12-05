print("..........<CALCULATOR>.................")
print(".......................................")


"""
adddition, substraction, multiplication, division, remainder, power, quotient, even/odd,

"""

while True :
    print(".......................................")
    print("Choose your operation: \n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Remainder (%)")
    print("6. Power (**)")
    print("7. Quotient (//)")
    print("8. Even/Odd Check")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 9:
        print("Calculator closed")
        break  #terminate the loop and exit the calculator
    
    if choice < 1 or choice > 9:
        print(" PLease try again. Your choice is invalid.")
        break  #terminate the loop and exit the calculator
    
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))

    if choice == 1:
        add = n1 + n2
        print(f"Addition result is {add} ")
        
    elif choice == 2:
        sub = n1 - n2
        print(f"Substraction result is {sub}")

    elif choice == 3:
        multiply = n1 * n2
        print(f"Multiplication result is {multiply}")
        
    elif choice == 4:
        division = n1/n2
        print(f"Division result is {division} ")
        
    elif choice == 5:
        remainder = n1 % n2
        print(f"Remainder is {remainder}")
        
    elif choice == 6:
        power = n1 ** n2
        print(f"power result is {power}")

    elif choice == 7:
        quotient = n1 // n2
        print(f"Quotient is {quotient}")

    elif choice == 8:
        
        if n1 % 2 == 0:
            print(f"{n1} is an even number")
        else:
            print(f"{n1} is an odd number")
            
        if n2 % 2 == 0:
            print(f"{n2} is an even number")
        else:
            print(f"{n2} is an odd number")

 
        
        