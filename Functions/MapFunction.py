# def temp_conv(c):
#     return 9/5 * c + 32

def temp_conv(c): return 9/5 * c + 32

# f = temp_conv(34.5)
# print(f)

temperatures = [34.5,43.2,29.5,41.2,26.5,32.3]

# data = []
# for t in temperatures:
#     data.append(temp_conv(t))
#
# print(data)

# def myMap(func,iter):
#     data = []
#     for i in range(len(iter)):
#         data.append(func(iter[i]))
#     return data
#
# data = myMap(temp_conv,temperatures)
# print(data)

# data = list(map(temp_conv,temperatures))
# print(data)

# a = lambda x,y,z : x + y + z
# print(a(1,2,3))

data = list(map(lambda c : 9/5 * c + 32,temperatures))
print(data)
