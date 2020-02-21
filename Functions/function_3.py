# Arguments -> Positional Args
# def add(x,y):
#     z = x + y
#     print("Sum is",z)
#
# add(4,5)
# add(x=12,y=21)
# add(y=22,x=10)

# Arguments -> Default Arguments
def add(x=0,y=0):
    z = x + y
    print("Sum is",z)

add()
add(4)
add(5,6)
add(x=12,y=21)
add(y=22,x=10)