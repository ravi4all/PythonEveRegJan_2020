# Return Statement
def add(x,y):
    z = x + y
    # print(z)
    return z

def showRes():
    z = add(4, 5)
    print("Result is",z)

showRes()

def calc(x,y):
    return x + y, x - y, x / y, x * y

# z = calc(4,5)
# print(z)
a,b,c,d = calc(4,5)
print(a,b,c,d)
