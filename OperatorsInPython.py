'''
Airthmetic Operator - +, - ,/ ,*, //, **, %
Comparison Operator - ==, >, <, >=, <=, !=
Logical Operator - and, or, not
Membership Operators - in, not in
Identity Operators - is, not is
'''

# Guess the number
import random

random_num = random.randint(1,100)

while (num := int(input("Enter a number : "))):
    if random_num == num:
        print("Congrats, You guessed the number...")
        break
    elif num > random_num:
        print("Too High...")
    elif num < random_num:
        print("Too Low...")
    elif random_num > 100 or random_num < 1:
        print("Invalid Number")
    else:
        print("Invalid Input...")
        
