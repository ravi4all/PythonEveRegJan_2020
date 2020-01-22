'''
1
10
101
1010
10101
'''

for i in range(1,6):
    for j in range(0,i):
        if j % 2 == 0:
            print('1',end='')
        else:
            print('0',end='')
    print()
print("="*20)

'''
1
01
010
1010
10101
'''
k = 0
for i in range(1,6):
    for j in range(0,i):
        k += 1
        if k % 2 == 0:
            print('0',end='')
        else:
            print('1',end='')
    print()
print("="*20)
