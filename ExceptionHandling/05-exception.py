def atm():
    total = 10000
    pin = input("Enter your pin : ")

    assert (pin == "1234"), "Login Failed"
    amount = int(input("Enter amount : "))

    assert (amount < total), "Insufficient balance"
    total -= amount
    print("Remaining balance is",total)

try:
    atm()
except ValueError as err:
    print(err)
except AssertionError as err:
    print(err)