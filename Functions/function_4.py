# *args -> Dynamic args - Variable length arguments
def add(*x):
    count = 0
    # for i in range(len(x)):
    #     count += x[i]
    # print("Sum is",count)
    print(sum(x))

add(3,4)
add(5,6,7,98)
add(1,3,4,7,8,9)

# **kwargs - keyword arguments
def emp(**details):
    print(details)

emp(name='Ram',dept='IT')
emp(name='Shyam',sal=123400,dept='IT',address='Delhi')
emp(name='Ramesh',sal=123400,dept='IT')