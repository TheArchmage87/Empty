print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
x=input("")
if x=="1":
    y=int(input("Number 1"))
    z=int(input("Number 2"))
    print(y+z)
elif x=="2":
    y=int(input("Number 1"))
    z=int(input("Number 2"))
    print(y-z)
elif x=="3":
    y=int(input("Number 1"))
    z=int(input("Number 2"))
    print(y*z)
elif x=="4":
    y=int(input("Number 1"))
    z=int(input("Number 2"))
    print(y/z)
elif x=="5":
    print("Bye!")
else:
    print("Error")