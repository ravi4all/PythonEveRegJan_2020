x = 11
y = 5

# Function definition
def add():
    global x
    global y
    x = 21
    y = 11
    z = x + y
    print("Sum is",z)

# Function Calling
add()
print(x-y)