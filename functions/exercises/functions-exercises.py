# Part 1 A -- Make a Line
def makeline(size):
    line = ""
    for i in range(size):
        line += "#"
    return line

print(makeline(5))
print("\n")

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def makesquare(size):
    square = ""
    for i in range(size):
        square += makeline(5) + "\n"
    return square

print(makesquare(5))

# Part 1 C -- Make a Rectangle
def makerectangle(width,length):
    rectangle = ""
    for i in range(length):
        rectangle += makeline(width) + "\n"
    return rectangle

print(makerectangle(5,3))

# Part 2 A -- Make a Stairs
def makestairs(size):
    stairs = ""
    for i in range(size):
        stairs += makeline(i+1) + "\n"
    return stairs

print(makestairs(5))

# Part 2 B -- Make Space-Line 
def makespace_line(spaces,chars):
    line = ""
    for i in range(spaces):
        line += " "
    line += makeline(chars)
    for i in range(spaces):
        line += " "
    return line

print(makespace_line(3,5))
print("\n")

# Part 2 C -- Make Isosceles Triangle
def makeisoceles_triangle(height):
    triangle = ""
    for i in range(height):
        triangle += makespace_line(height - i - 1, 2 * i + 1) + "\n"
    return triangle

print(makeisoceles_triangle(5))

# Part 3 -- Make a Diamond
def makediamond(height):
    diamond = ""
    triangle = makeisoceles_triangle(height)
    diamond += triangle[:-1]
    for i in range(len(triangle)-1, -1, -1):
      diamond += triangle[i]
    return diamond

print(makediamond(5))





