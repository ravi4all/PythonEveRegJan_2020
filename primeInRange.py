num_1 = int(input("Enter min range : "))
num_2 = int(input("Enter max range : "))

for num in range(num_1, num_2+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                #print("Not Prime")
                break
        else:
            print("Prime Number",num)
