def atm():
    total = 10000
    pin = input("Enter your pin : ")
    if pin == "1234":
        print("Login Success")
    else:
        raise ValueError("Login Failed")

    amount = int(input("Enter amount : "))
    if amount < total:
        total -= amount
        print("Remaining bal is",total)
    else:
        raise ValueError("Insufficient Balance")

try:
    atm()
except ValueError as err:
    print(err)