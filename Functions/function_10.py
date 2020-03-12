def outer():
    x = 11
    y = 12

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    return add,sub

def calc():
    ch = input("Enter your choice : ")
    x1 = outer()
    if ch == "1":
        z = x1[0]()
        print("Addition is",z)
    else:
        z = x1[1]()
        print("Subtraction is",z)

calc()