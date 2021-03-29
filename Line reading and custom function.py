a = open("text.txt")
p = a.readlines()
for line in p:
    print(line)

z = "Hello world, this is a test sentence to test code using a test sentence"
y = z.split("world")

print(y)

b = str(input("What is your name?"))
def pencilpouch(name):
    print("Hello! How are you today, ",name, "?") 

pencilpouch(b)
