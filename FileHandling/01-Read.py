file = open('data_1.txt','r')

# data = file.read()

# data = file.read(10)

# data = file.readline()

# data = file.readlines()

file.seek(6)
data = file.read()
print(data)

file.close()