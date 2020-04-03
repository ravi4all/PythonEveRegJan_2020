def calc():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a + b
    print("Sum is", c)

    d = a - b
    print("Diff is", d)

    e = a / b
    print("Div is", e)

    f = a * b
    print("Mul is", f)

try:
    calc()
except ValueError:
    print("Invalid Input")
    calc()
except ZeroDivisionError:
    print("Cannot divide by zero")
    calc()
except BaseException as ex:
    print(ex)
    calc()

