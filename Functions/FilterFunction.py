# def even(num):
#     return num % 2 == 0
#
# n = even(12)
# print(n)

numbers = [3,5,7,9,9,1,2,2,3,4,6,7,9,0,8,6,4,4,12]

# n = list(map(even,numbers))
# print(n)

# n = list(filter(even,numbers))
# print(n)

data = list(filter(lambda n : n % 2 == 0, numbers))
print(data)
