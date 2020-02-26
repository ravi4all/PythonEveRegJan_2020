def getInput():
    f_num = int(input("Enter first number : "))
    s_num = int(input("Enter second number : "))
    return f_num,s_num

def add():
    x,y = getInput()
    z = x + y
    print("Sum is",z)

def sub():
    x, y = getInput()
    z = x - y if x > y else y - x
    print("Diff is",z)

def div():
    x, y = getInput()
    z = x / y
    print("Div is",z)

def mul():
    x, y = getInput()
    z = x * y
    print("Mul is",z)

def errHandler(*args,**kwargs):
    print("Invalid Choice...")

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

operations = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}
operations.get(ch,errHandler)()