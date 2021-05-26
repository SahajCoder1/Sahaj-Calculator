print("Welcome to Sahaj Calculator")
print("What you want, Addition, Substraction, Multiplication, Divison " 
                   + "Plese enter what you want")


want = input("Enter what you want: ")

if want == "Addition":
    print("Ok")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("The sum of first number and second number is", a + b)

if want == "Substraction":
    print("Ok")
    c = int(input("Enter first number: "))
    d = int(input("Enter second number: "))
    print("The Substraction of first number and second number is", c - d)

if want == "Multiplication":
    print("Ok")
    e = int(input("Enter first number: "))
    f = int(input("Enter second number: "))
    print("The Multiplication of first number and second number is", e * f)

if want == "Divison" :
    print("Ok")
    g = int(input("Enter first number: "))
    h = int(input("Enter second number: "))
    print("The Divison of first number and second number is", g / h)

print("Thanks for using Sahaj Calculator")
print("Type any key to exit")
exitt = input("Exit: ")
