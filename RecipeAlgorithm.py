print("Step one: Get a glass of cold milk")
a = input("Is the milk cold?")
if(a == "no"):
    print("Make the milk cold then")
    a = input("Is the milk cold?")
    print("Add coffee powder, sugar and ice cubes to the milk")
else:
    print("Add coffee powder, sugar and ice cubes to the milk")

b = input("Have you added the ingredients?")
if(b == "no"):
    print("Add them then")
    b = input("Have you added the ingredients?")
    print("Pour into a blender and blend")
else:
    print("Pour into a blender and blend")

c = input("Have the ingredients blended?")
if(c == "no"):
    print("Blend them then")
    c = input("Have the ingredients blended?")
    print("Pour into a cup and enjoy :D")
else:
    print("Pour into a cup and enjoy :D")