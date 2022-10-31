totalarea = int(input("Please enter the total area of the room you would like to paint "))
nonpaintarea = int(input("Please enter the total unpaintable area "))
coats = int(input("Please enter the number of coats required "))

paintarea = totalarea - nonpaintarea

paint = (paintarea * coats) // 11

paint = paint + 1

print("The total number of cans of paint required is ", paint)