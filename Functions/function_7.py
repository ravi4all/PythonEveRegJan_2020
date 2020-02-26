def getInput():
    f_num = input("Enter first number : ")
    s_num = input("Enter second number : ")
    return f_num,s_num

def calc(opr):
    x,y = getInput()
    res = eval(x+opr+y)
    print(res)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

operations = {
    "1" : "+",
    "2" : "-",
    "3" : "/",
    "4" : "*"
}
opr = operations.get(ch)
calc(opr)