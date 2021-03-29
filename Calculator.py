print("Hello! this is a calculator! :D")

z = str(input("Kindly choose an operation to perform: "))


if(z == "addition"):
    a = int (input("Kindly enter the first value: "))
    b = int (input("Kindly enter the second value: "))
    c = a + b 
    print("The answer is ", c)
elif(z == "subtraction"):
    a = int (input("Kindly enter the first value: "))
    b = int (input("Kindly enter the second value: "))
    c = a - b 
    print("The answer is ", c)
elif(z == "multiplication"):
    a = int (input("Kindly enter the first value: "))
    b = int (input("Kindly enter the second value: "))
    c = a * b 
    print("The answer is ", c)
else:
    a = int (input("Kindly enter the first value: "))
    b = int (input("Kindly enter the second value: "))
    c = a / b 
    print("The answer is ", c)

