def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y if x > y else y - x
    print("Diff is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

def mul(x,y):
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
f_num = int(input("Enter first number : "))
s_num = int(input("Enter second number : "))

# operations = [add,sub,div,mul]
# operations[int(ch) - 1](f_num,s_num)

operations = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}
operations.get(ch,errHandler)(f_num,s_num)