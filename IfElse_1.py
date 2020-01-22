name = input("Enter your name : ")
print("Welcome",name)

# print("Welcome",name := input("Enter your name : "))

num = int(input("Enter a number : "))
if num % 2 == 0:
    print("Even Number")
elif num % 2 != 0:
    print("Odd Number")
else:
    print("Not a number")
