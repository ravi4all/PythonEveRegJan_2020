try:
    file = open('file_1.txt','r')
    data = file.read()
except FileNotFoundError:
    print("File Not Found")
    print("Creating file")
    file = open('file_1.txt','w')
else:
    print(data)
finally:
    file.close()