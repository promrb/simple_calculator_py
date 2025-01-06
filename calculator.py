print("*******************")                                              
print("** MY CALCULATOR **")
print("*******************")

x = input("Enter Input Number 1: ")
print("What do you want to do?")
n = input("Enter any operation (+, -, *, /): ")
y = input("Enter Input Number 2: ")


if n == "+" :
    z=float(x) + float(y)
elif n  == "-" : 
    z=float(x) - float(y)
elif n == "*" :
    z=float(x) * float(y)
elif n == "/" :
    z=float(x) / float(y)
else:
    print("ERROR: Wrong Operation Selected")
    exit(0)

print (f"Answer of {float(x)}  {(n)}  {float(y)} = {float(z)}")
