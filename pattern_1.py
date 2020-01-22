'''
*
**
***
****
*****
'''
'''
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()
print("="*10)
'''
# Alternative
for i in range(1,6):
    for j in range(i):
        print('*',end='')
    print()
print("="*10)

'''
*****
****
***
**
*
'''
for i in range(5,0,-1):
    for j in range(i):
        print('*',end='')
    print()
print("="*10)

'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(i):
        print(j+1,end='')
    print()
print("="*10)

'''
1
23
456
78910
'''
a = 0
for i in range(1,5):
    for j in range(i):
        a += 1
        print(a,end='')
    print()
print("="*10)
