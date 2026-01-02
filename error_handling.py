try:
    with open("C:/Users/sigde/OneDrive/Desktop/Python/test.txt","r") as f:
        print(f.read())
        
except FileNotFoundError:
    print("FIle not found")
    
    
print("Program running")
