num = int(input("Enter a number : "))

'''
prime = False
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            #print("Not Prime")
            prime = False
            break
        else:
            prime = True
            #print("Prime Number")

if prime:
    print("Prime Number")
else:
    print("Not Prime")
'''

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
